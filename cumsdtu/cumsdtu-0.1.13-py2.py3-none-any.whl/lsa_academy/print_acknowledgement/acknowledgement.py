import redis

from cumsdtu.utils.persist_cookies import PersistCookies
from cumsdtu.lsa_academy.logins.login import Login
from cumsdtu.model.lsa_model import ManageCredentials

class Acknowledgement(Login):

    get_ack_url = 'https://cumsdtu.in/LSARegistration/api/acknldgmnt?instId=1'
    applicant_class = ManageCredentials

    def __init__(self, to_verify, **kwargs):
        super().__init__(to_verify, **kwargs)
        self.to_verify = to_verify
        self.persistor = self.safe_dict(kwargs, 'persistor')
        self.ack_file_name = self.safe_dict(kwargs,'ack_file')
        self.is_force = self.safe_dict(kwargs,'is_force',False)

    def pre_query(self):

        if not self.reg_data.get('status') and not self.is_force:
            return self.custom_response(True,"Status is Incomplete",400)

        if self.is_force and not self.reg_data.get('remainingCourses') ==0:
            return self.custom_response(True,"Minimum course requirement not satisfied, need {} more courses.".format(self.reg_data.get('remainingCourses')),400)

        if self.is_force and not self.reg_data.get('remainingCredit') == 0:
            return self.custom_response(True, "Minimum credits requirement not satisfied, need {} more credits.".format(
                self.reg_data.get('remainingCredit')), 400)

        response = self.smart_request('GET',self.get_ack_url,headers = self.headers)

        json_data= self.safe_json(response.text)

        if json_data.get('error'):
            return self.custom_response(True,json_data.get('msgLst'),409)

        return self.query_info(ack_url=json_data.get('data')[-1])

    def query_info(self, **kwargs):

        self.headers['host'] = 'lsacdn.lsnetx.com'

        resposne=self.smart_request('GET',kwargs.get('ack_url'),headers = self.headers)

        file_name=self.ack_file_name if self.ack_file_name.endswith('.pdf') else self.ack_file_name+'.pdf'

        file = open(file_name,'wb')
        file.write(resposne.content)
        file.close()

        return self.custom_response(False,"File save successfully at {}".format(file_name),200,file_name=file_name)

    @classmethod
    def extract_data(cls, db_ob, **kwargs):
        applicant = cls.applicant_class.applicant_to_object(db_ob)

        login_data = Login.do_login(applicant, **kwargs)

        if login_data.get('status') != 200:
            return login_data

        return cls(applicant, **{**login_data.pop('data'), **login_data, **kwargs}).pre_query()


def test():
    applicant = ManageCredentials()
    applicant.username = '2K19/ME/051'
    applicant.password = 'April@2000'

    r = redis.Redis(host='redis-13748.c14.us-east-1-2.ec2.cloud.redislabs.com',
                    port=13748,
                    password='KfhZsGRLZ0aqDzT4pl1K4BmfrFbrpaGn')

    # r = redis.StrictRedis()

    persistor = PersistCookies(r, 'cumsdtu:{}'.format(applicant.username.replace('/', '_')))

    return Acknowledgement.extract_data(applicant,persistor=persistor,is_force=True,ack_file=applicant.username.replace('/', '_')+'.pdf')


if __name__ == '__main__':
    print(test())
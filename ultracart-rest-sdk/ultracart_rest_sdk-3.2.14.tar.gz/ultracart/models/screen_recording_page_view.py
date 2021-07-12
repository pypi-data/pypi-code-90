# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ScreenRecordingPageView(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain': 'str',
        'events': 'list[ScreenRecordingPageViewEvent]',
        'first_event_timestamp': 'str',
        'http_post': 'bool',
        'last_event_timestamp': 'str',
        'missing_events': 'bool',
        'params': 'list[ScreenRecordingPageViewParameter]',
        'range_end': 'int',
        'range_start': 'int',
        'referrer': 'str',
        'referrer_params': 'list[ScreenRecordingPageViewParameter]',
        'referrer_raw': 'str',
        'screen_recording_page_view_uuid': 'str',
        'time_on_page': 'int',
        'timing_dom_content_loaded': 'int',
        'timing_loaded': 'int',
        'truncated_events': 'bool',
        'ucapv': 'str',
        'url': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'events': 'events',
        'first_event_timestamp': 'first_event_timestamp',
        'http_post': 'http_post',
        'last_event_timestamp': 'last_event_timestamp',
        'missing_events': 'missing_events',
        'params': 'params',
        'range_end': 'range_end',
        'range_start': 'range_start',
        'referrer': 'referrer',
        'referrer_params': 'referrer_params',
        'referrer_raw': 'referrer_raw',
        'screen_recording_page_view_uuid': 'screen_recording_page_view_uuid',
        'time_on_page': 'time_on_page',
        'timing_dom_content_loaded': 'timing_dom_content_loaded',
        'timing_loaded': 'timing_loaded',
        'truncated_events': 'truncated_events',
        'ucapv': 'ucapv',
        'url': 'url'
    }

    def __init__(self, domain=None, events=None, first_event_timestamp=None, http_post=None, last_event_timestamp=None, missing_events=None, params=None, range_end=None, range_start=None, referrer=None, referrer_params=None, referrer_raw=None, screen_recording_page_view_uuid=None, time_on_page=None, timing_dom_content_loaded=None, timing_loaded=None, truncated_events=None, ucapv=None, url=None):  # noqa: E501
        """ScreenRecordingPageView - a model defined in Swagger"""  # noqa: E501

        self._domain = None
        self._events = None
        self._first_event_timestamp = None
        self._http_post = None
        self._last_event_timestamp = None
        self._missing_events = None
        self._params = None
        self._range_end = None
        self._range_start = None
        self._referrer = None
        self._referrer_params = None
        self._referrer_raw = None
        self._screen_recording_page_view_uuid = None
        self._time_on_page = None
        self._timing_dom_content_loaded = None
        self._timing_loaded = None
        self._truncated_events = None
        self._ucapv = None
        self._url = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if events is not None:
            self.events = events
        if first_event_timestamp is not None:
            self.first_event_timestamp = first_event_timestamp
        if http_post is not None:
            self.http_post = http_post
        if last_event_timestamp is not None:
            self.last_event_timestamp = last_event_timestamp
        if missing_events is not None:
            self.missing_events = missing_events
        if params is not None:
            self.params = params
        if range_end is not None:
            self.range_end = range_end
        if range_start is not None:
            self.range_start = range_start
        if referrer is not None:
            self.referrer = referrer
        if referrer_params is not None:
            self.referrer_params = referrer_params
        if referrer_raw is not None:
            self.referrer_raw = referrer_raw
        if screen_recording_page_view_uuid is not None:
            self.screen_recording_page_view_uuid = screen_recording_page_view_uuid
        if time_on_page is not None:
            self.time_on_page = time_on_page
        if timing_dom_content_loaded is not None:
            self.timing_dom_content_loaded = timing_dom_content_loaded
        if timing_loaded is not None:
            self.timing_loaded = timing_loaded
        if truncated_events is not None:
            self.truncated_events = truncated_events
        if ucapv is not None:
            self.ucapv = ucapv
        if url is not None:
            self.url = url

    @property
    def domain(self):
        """Gets the domain of this ScreenRecordingPageView.  # noqa: E501


        :return: The domain of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ScreenRecordingPageView.


        :param domain: The domain of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def events(self):
        """Gets the events of this ScreenRecordingPageView.  # noqa: E501


        :return: The events of this ScreenRecordingPageView.  # noqa: E501
        :rtype: list[ScreenRecordingPageViewEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ScreenRecordingPageView.


        :param events: The events of this ScreenRecordingPageView.  # noqa: E501
        :type: list[ScreenRecordingPageViewEvent]
        """

        self._events = events

    @property
    def first_event_timestamp(self):
        """Gets the first_event_timestamp of this ScreenRecordingPageView.  # noqa: E501

        First event timestamp  # noqa: E501

        :return: The first_event_timestamp of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._first_event_timestamp

    @first_event_timestamp.setter
    def first_event_timestamp(self, first_event_timestamp):
        """Sets the first_event_timestamp of this ScreenRecordingPageView.

        First event timestamp  # noqa: E501

        :param first_event_timestamp: The first_event_timestamp of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._first_event_timestamp = first_event_timestamp

    @property
    def http_post(self):
        """Gets the http_post of this ScreenRecordingPageView.  # noqa: E501


        :return: The http_post of this ScreenRecordingPageView.  # noqa: E501
        :rtype: bool
        """
        return self._http_post

    @http_post.setter
    def http_post(self, http_post):
        """Sets the http_post of this ScreenRecordingPageView.


        :param http_post: The http_post of this ScreenRecordingPageView.  # noqa: E501
        :type: bool
        """

        self._http_post = http_post

    @property
    def last_event_timestamp(self):
        """Gets the last_event_timestamp of this ScreenRecordingPageView.  # noqa: E501

        Last event timestamp  # noqa: E501

        :return: The last_event_timestamp of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._last_event_timestamp

    @last_event_timestamp.setter
    def last_event_timestamp(self, last_event_timestamp):
        """Sets the last_event_timestamp of this ScreenRecordingPageView.

        Last event timestamp  # noqa: E501

        :param last_event_timestamp: The last_event_timestamp of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._last_event_timestamp = last_event_timestamp

    @property
    def missing_events(self):
        """Gets the missing_events of this ScreenRecordingPageView.  # noqa: E501


        :return: The missing_events of this ScreenRecordingPageView.  # noqa: E501
        :rtype: bool
        """
        return self._missing_events

    @missing_events.setter
    def missing_events(self, missing_events):
        """Sets the missing_events of this ScreenRecordingPageView.


        :param missing_events: The missing_events of this ScreenRecordingPageView.  # noqa: E501
        :type: bool
        """

        self._missing_events = missing_events

    @property
    def params(self):
        """Gets the params of this ScreenRecordingPageView.  # noqa: E501


        :return: The params of this ScreenRecordingPageView.  # noqa: E501
        :rtype: list[ScreenRecordingPageViewParameter]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ScreenRecordingPageView.


        :param params: The params of this ScreenRecordingPageView.  # noqa: E501
        :type: list[ScreenRecordingPageViewParameter]
        """

        self._params = params

    @property
    def range_end(self):
        """Gets the range_end of this ScreenRecordingPageView.  # noqa: E501


        :return: The range_end of this ScreenRecordingPageView.  # noqa: E501
        :rtype: int
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """Sets the range_end of this ScreenRecordingPageView.


        :param range_end: The range_end of this ScreenRecordingPageView.  # noqa: E501
        :type: int
        """

        self._range_end = range_end

    @property
    def range_start(self):
        """Gets the range_start of this ScreenRecordingPageView.  # noqa: E501


        :return: The range_start of this ScreenRecordingPageView.  # noqa: E501
        :rtype: int
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this ScreenRecordingPageView.


        :param range_start: The range_start of this ScreenRecordingPageView.  # noqa: E501
        :type: int
        """

        self._range_start = range_start

    @property
    def referrer(self):
        """Gets the referrer of this ScreenRecordingPageView.  # noqa: E501


        :return: The referrer of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this ScreenRecordingPageView.


        :param referrer: The referrer of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._referrer = referrer

    @property
    def referrer_params(self):
        """Gets the referrer_params of this ScreenRecordingPageView.  # noqa: E501


        :return: The referrer_params of this ScreenRecordingPageView.  # noqa: E501
        :rtype: list[ScreenRecordingPageViewParameter]
        """
        return self._referrer_params

    @referrer_params.setter
    def referrer_params(self, referrer_params):
        """Sets the referrer_params of this ScreenRecordingPageView.


        :param referrer_params: The referrer_params of this ScreenRecordingPageView.  # noqa: E501
        :type: list[ScreenRecordingPageViewParameter]
        """

        self._referrer_params = referrer_params

    @property
    def referrer_raw(self):
        """Gets the referrer_raw of this ScreenRecordingPageView.  # noqa: E501


        :return: The referrer_raw of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._referrer_raw

    @referrer_raw.setter
    def referrer_raw(self, referrer_raw):
        """Sets the referrer_raw of this ScreenRecordingPageView.


        :param referrer_raw: The referrer_raw of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._referrer_raw = referrer_raw

    @property
    def screen_recording_page_view_uuid(self):
        """Gets the screen_recording_page_view_uuid of this ScreenRecordingPageView.  # noqa: E501


        :return: The screen_recording_page_view_uuid of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._screen_recording_page_view_uuid

    @screen_recording_page_view_uuid.setter
    def screen_recording_page_view_uuid(self, screen_recording_page_view_uuid):
        """Sets the screen_recording_page_view_uuid of this ScreenRecordingPageView.


        :param screen_recording_page_view_uuid: The screen_recording_page_view_uuid of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._screen_recording_page_view_uuid = screen_recording_page_view_uuid

    @property
    def time_on_page(self):
        """Gets the time_on_page of this ScreenRecordingPageView.  # noqa: E501


        :return: The time_on_page of this ScreenRecordingPageView.  # noqa: E501
        :rtype: int
        """
        return self._time_on_page

    @time_on_page.setter
    def time_on_page(self, time_on_page):
        """Sets the time_on_page of this ScreenRecordingPageView.


        :param time_on_page: The time_on_page of this ScreenRecordingPageView.  # noqa: E501
        :type: int
        """

        self._time_on_page = time_on_page

    @property
    def timing_dom_content_loaded(self):
        """Gets the timing_dom_content_loaded of this ScreenRecordingPageView.  # noqa: E501

        Amount of time for DOMContentLoaded event to fire (milliseconds)  # noqa: E501

        :return: The timing_dom_content_loaded of this ScreenRecordingPageView.  # noqa: E501
        :rtype: int
        """
        return self._timing_dom_content_loaded

    @timing_dom_content_loaded.setter
    def timing_dom_content_loaded(self, timing_dom_content_loaded):
        """Sets the timing_dom_content_loaded of this ScreenRecordingPageView.

        Amount of time for DOMContentLoaded event to fire (milliseconds)  # noqa: E501

        :param timing_dom_content_loaded: The timing_dom_content_loaded of this ScreenRecordingPageView.  # noqa: E501
        :type: int
        """

        self._timing_dom_content_loaded = timing_dom_content_loaded

    @property
    def timing_loaded(self):
        """Gets the timing_loaded of this ScreenRecordingPageView.  # noqa: E501

        Amount of time for loaded event to fire (milliseconds)  # noqa: E501

        :return: The timing_loaded of this ScreenRecordingPageView.  # noqa: E501
        :rtype: int
        """
        return self._timing_loaded

    @timing_loaded.setter
    def timing_loaded(self, timing_loaded):
        """Sets the timing_loaded of this ScreenRecordingPageView.

        Amount of time for loaded event to fire (milliseconds)  # noqa: E501

        :param timing_loaded: The timing_loaded of this ScreenRecordingPageView.  # noqa: E501
        :type: int
        """

        self._timing_loaded = timing_loaded

    @property
    def truncated_events(self):
        """Gets the truncated_events of this ScreenRecordingPageView.  # noqa: E501


        :return: The truncated_events of this ScreenRecordingPageView.  # noqa: E501
        :rtype: bool
        """
        return self._truncated_events

    @truncated_events.setter
    def truncated_events(self, truncated_events):
        """Sets the truncated_events of this ScreenRecordingPageView.


        :param truncated_events: The truncated_events of this ScreenRecordingPageView.  # noqa: E501
        :type: bool
        """

        self._truncated_events = truncated_events

    @property
    def ucapv(self):
        """Gets the ucapv of this ScreenRecordingPageView.  # noqa: E501


        :return: The ucapv of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._ucapv

    @ucapv.setter
    def ucapv(self, ucapv):
        """Sets the ucapv of this ScreenRecordingPageView.


        :param ucapv: The ucapv of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._ucapv = ucapv

    @property
    def url(self):
        """Gets the url of this ScreenRecordingPageView.  # noqa: E501


        :return: The url of this ScreenRecordingPageView.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ScreenRecordingPageView.


        :param url: The url of this ScreenRecordingPageView.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScreenRecordingPageView, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScreenRecordingPageView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

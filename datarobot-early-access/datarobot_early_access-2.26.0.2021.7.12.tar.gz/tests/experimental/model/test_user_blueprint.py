import json

import pytest
import responses
import six
import six.moves.urllib.parse as urllibparse

from datarobot._experimental import UserBlueprint
from datarobot._experimental.models.user_blueprints.models import (
    DEFAULT_BATCH_SIZE,
    GrantAccessControlWithUsernameValidator,
    UserBlueprintAddToProjectMenu,
    UserBlueprintAvailableInput,
    UserBlueprintAvailableTasks,
    UserBlueprintCatalogSearch,
    UserBlueprintSharingListController,
    UserBlueprintValidateTaskParameters,
)
from datarobot.utils import from_api, to_api


def as_shallow_dict(item):
    return {
        k: v for k, v in six.iteritems(item.__dict__) if not k.startswith("_") and not callable(v)
    }


@pytest.fixture
def mock_role():
    return {
        "share_recipient_type": "user",
        "role": "OWNER",
        "id": "".join(["a"] * 24),
        "name": "test-user@datarobot.com",
    }


@pytest.fixture
def mock_roles_response(mock_role):
    return {"count": 1, "next": None, "previous": None, "data": [mock_role], "total_count": 1}


def build_mocked_task(name):
    return {
        "taskCode": name,
        "taskDefinition": {
            "customTaskId": None,
            "taskCode": "ABC",
            "description": (
                "AdaBoost Classifier (scikit-learn). An AdaBoost classifier "
                "is a meta-estimator that begins by fitting a classifier on the "
                "original dataset and then fits additional copies of the classifier "
                "on the same dataset but where the weights of incorrectly classified "
                "instances are adjusted such that subsequent classifiers focus more on "
                "difficult cases."
            ),
            "url": {"DataRobot Model Docs": "/model-docs/tasks/ABC-Adaboost-Classifier.html"},
            "sparseInputSupportLevel": "forbidden",
            "isCustomTask": None,
            "sparseInput": False,
            "categories": ["Adaptive Boosting Classifier"],
            "validInputs": ["NUM"],
            "label": "Adaboost Classifier",
            "colnamesAndTypes": [
                {"colname": "a", "hex": "61", "type": "NUM"},
                {"colname": "b", "hex": "62", "type": "NUM"},
            ],
            "arguments": [
                {
                    "argument": {
                        "default": "1234",
                        "values": [0, 1000000000],
                        "recommended": 1234,
                        "type": "int",
                        "name": "random_state",
                    },
                    "key": "rs",
                },
            ],
            "outputMethods": ["P", "S"],
            "hasSparseOutput": "unknown",
            "timeSeriesOnly": False,
            "outputsNonnumericInputType": False,
            "icon": 1,
            "customTaskVersions": [
                {"id": "abc", "versionMajor": -1, "versionMinor": -1, "label": "A"}
            ],
        },
    }


@pytest.fixture
def mocked_available_tasks():
    task = build_mocked_task("DEF")
    task["taskDefinition"]["supportsScoringCode"] = False
    return {
        "tasks": [build_mocked_task("ABC"), task],
        "categories": [
            {
                "name": "Adaptive Boosting Classifier",
                "taskCodes": ["ABC"],
                "subcategories": [{"name": "Adaptive Boosting Classifier", "taskCodes": ["ABC"]}],
            }
        ],
    }


@pytest.fixture
def mocked_validated_task_parameters():
    return {
        "errors": [
            {"paramName": "learning_rate", "message": "Invalid value(s) supplied", "value": "abc"},
        ],
    }


@pytest.fixture
def mocked_input_types():
    long_name_lookup = {
        "NUM": "Numeric",
        "CAT": "Categorical",
        "TXT": "Text",
    }
    return {
        "inputTypes": sorted(
            [{"type": _type, "name": name} for _type, name in six.iteritems(long_name_lookup)],
            key=lambda x: x["type"],
        )
    }


@pytest.fixture
def mocked_add_to_menu_response(blueprint_id, user_blueprint_id):
    return {"addedToMenu": [{"userBlueprintId": user_blueprint_id, "blueprintId": blueprint_id}]}


@pytest.fixture
def blueprint():
    return [
        {
            "task_data": {
                "inputs": ["CAT"],
                "output_method": "T",
                "task_code": "ORDCAT2",
                "output_method_parameters": [],
                "x_transformations": [],
                "task_parameters": [
                    {"value": False, "param": "acm"},
                    {"value": False, "param": "amm"},
                    {"value": 5, "param": "ms"},
                    {"value": False, "param": "np_dtype_fix"},
                    {"value": True, "param": "o"},
                    {"value": 0, "param": "os"},
                    {"value": True, "param": "r"},
                    {"value": 1234, "param": "s"},
                ],
                "y_transformations": [],
            },
            "task_id": u"1",
        },
        {
            "task_data": {
                "inputs": ["NUM"],
                "output_method": "T",
                "task_code": "PNI2",
                "output_method_parameters": [],
                "x_transformations": [],
                "task_parameters": [
                    {"value": False, "param": "np_dtype_fix"},
                    {"value": False, "param": "s"},
                    {"value": 10, "param": "t"},
                ],
                "y_transformations": [],
            },
            "task_id": u"2",
        },
        {
            "task_data": {
                "inputs": [u"1", u"2"],
                "output_method": "P",
                "task_code": u"ESXGBC2",
                "output_method_parameters": [],
                "x_transformations": [],
                "task_parameters": [
                    {"value": 1, "param": "b_n"},
                    {"value": 1, "param": "b_nj"},
                    {"value": 1234, "param": "b_rs"},
                    {"value": False, "param": "base_init"},
                    {"value": 1.0, "param": "cbl"},
                    {"value": 1.0, "param": "cbt"},
                    {"value": u"deviance", "param": "l"},
                    {"value": None, "param": u"logy"},
                    {"value": 0.5, "param": "lr"},
                    {"value": 256, "param": "mb"},
                    {"value": 1.0, "param": "mcw"},
                    {"value": 3, "param": "md"},
                    {"value": 0.0, "param": "mds"},
                    {"value": 0.01, "param": "msl"},
                    {"value": 0.0, "param": "mv"},
                    {"value": 100, "param": "n"},
                    {"value": 1, "param": "npt"},
                    {"value": False, "param": "pp_mi"},
                    {"value": 5, "param": "pp_sf"},
                    {"value": True, "param": "pp_stk"},
                    {"value": 0, "param": "pp_stk_keep_top_n"},
                    {"value": False, "param": "pp_stk_seq"},
                    {"value": False, "param": "pp_stkm"},
                    {"value": False, "param": "pp_toboost"},
                    {"value": False, "param": "pp_wc"},
                    {"value": 0.0, "param": "ra"},
                    {"value": 1.0, "param": "rl"},
                    {"value": 1234, "param": "rs"},
                    {"value": 1.0, "param": "s"},
                    {"value": False, "param": "shap_center"},
                    {"value": False, "param": "shap_fit"},
                    {"value": 1.0, "param": "spw"},
                    {"value": 0, "param": "sw_b"},
                    {"value": 0.25, "param": "sw_tf"},
                    {"value": u"Pattern Search", "param": "t_a"},
                    {"value": 1, "param": "t_bn"},
                    {"value": True, "param": "t_call_fit_grid"},
                    {"value": False, "param": "t_clustering_score_on_training"},
                    {"value": True, "param": "t_es"},
                    {"value": 5, "param": "t_es_init"},
                    {"value": 10, "param": "t_int"},
                    {"value": False, "param": "t_light"},
                    {"value": 15, "param": "t_mi"},
                    {"value": 5, "param": "t_n"},
                    {"value": 1234, "param": "t_rs"},
                    {"value": True, "param": "t_s"},
                    {"value": False, "param": "t_sc"},
                    {"value": False, "param": "t_sf"},
                    {"value": 200, "param": "t_sint"},
                    {"value": 10, "param": "t_sp"},
                    {"value": u"auto", "param": "tm"},
                    {"value": False, "param": "wa_bw"},
                ],
                "y_transformations": [{"value": None, "param": u"logy"}],
            },
            "task_id": u"3",
        },
    ]


@pytest.fixture
def blueprint_id():
    return "9c0c01ad4b23f1b055813ceb730bafca"


@pytest.fixture
def user_id():
    return "60733a301445e1d1625ebec5"


@pytest.fixture
def project_id():
    return "60733d631445e1d1625ebec6"


@pytest.fixture
def user_blueprint_id():
    return "556cdfbb100d2b0e88585182"


@pytest.fixture
def mock_user_blueprint_without_blueprint(blueprint_id, user_blueprint_id, user_id):
    return {
        "blender": False,
        "blueprintId": blueprint_id,
        "diagram": "{}",
        "features": ["Keras Neural Network Classifier"],
        "featuresText": "Keras Neural Network Classifier",
        "icons": [4],
        "insights": "NA",
        "modelType": "Keras Neural Network Classifier",
        "referenceModel": False,
        "supportsGpu": True,
        "shapSupport": False,
        "supportsNewSeries": False,
        "userBlueprintId": user_blueprint_id,
        "userId": str(user_id),
        "vertexContext": [
            {
                "information": {
                    "inputs": [
                        "Missing Values: Forbidden",
                        "Data Type: Numeric",
                        "Sparsity: Supported",
                    ],
                    "outputs": ["Missing Values: Never", "Data Type: Numeric", "Sparsity: Never"],
                },
                "messages": {
                    "warnings": ["Unexpected input type. Expected Numeric, received All."]
                },
                "taskId": "1",
            }
        ],
        "supportedTargetTypes": ["binary"],
        "isTimeSeries": False,
        "hexColumnNameLookup": [],
        "customTaskVersionMetadata": [],
        "decompressedFormat": False,
    }


@pytest.fixture
def mock_user_blueprint(blueprint, mock_user_blueprint_without_blueprint):
    return dict(mock_user_blueprint_without_blueprint, blueprint=from_api(blueprint))


@pytest.fixture
def mock_user_blueprint_with_project_id(mock_user_blueprint, project_id):
    return dict(mock_user_blueprint, projectId=project_id)


@pytest.fixture
def make_url(unittest_endpoint):
    def _make_url(url):
        return "{}/{}".format(unittest_endpoint, url)

    return _make_url


@pytest.mark.parametrize("limit", [0, 10])
@responses.activate
def test_list_blueprints(make_url, mock_user_blueprint_without_blueprint, limit):
    original_limit = limit
    if limit == 0:
        limit = DEFAULT_BATCH_SIZE
    urlA = make_url("userBlueprints/?offset=3&limit={}").format(limit)
    urlB = make_url("userBlueprints/?limit={}&offset=3").format(limit)
    responses.add(
        responses.GET,
        urlA,
        status=200,
        content_type="application/json",
        body=json.dumps({"data": [mock_user_blueprint_without_blueprint], "next": None}),
    )
    response = UserBlueprint.list(limit=original_limit, offset=3)
    assert response == [UserBlueprint.from_server_data(mock_user_blueprint_without_blueprint)]
    assert responses.calls[0].request.method == "GET"
    assert responses.calls[0].request.url in [urlA, urlB]


@responses.activate
def test_get_blueprint(make_url, user_blueprint_id, mock_user_blueprint):
    urlA = make_url(
        "userBlueprints/{}/?editMode=True&decompressedBlueprint=True".format(user_blueprint_id)
    )
    urlB = make_url(
        "userBlueprints/{}/?decompressedBlueprint=True&editMode=True".format(user_blueprint_id)
    )
    responses.add(
        responses.GET,
        urlA,
        status=200,
        content_type="application/json",
        body=json.dumps(mock_user_blueprint),
    )
    response = UserBlueprint.get(user_blueprint_id)
    assert response == UserBlueprint.from_server_data(mock_user_blueprint)
    assert response == UserBlueprint(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "GET"
    assert responses.calls[0].request.url in [urlA, urlB]


@responses.activate
@pytest.mark.parametrize("pid, expected_pid", [(None, None), ("foo", "foo")])
@pytest.mark.parametrize("model_type, expected_model_type", [(None, None), ("foo", "foo")])
@pytest.mark.parametrize(
    "save_to_catalog, expected_save_to_catalog", [(None, True), (False, False)]
)
def test_create_blueprint_with_data(
    make_url,
    mock_user_blueprint,
    blueprint,
    pid,
    expected_pid,
    model_type,
    expected_model_type,
    save_to_catalog,
    expected_save_to_catalog,
):
    url = make_url("userBlueprints/")
    responses.add(
        responses.POST,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mock_user_blueprint),
    )

    kwargs = {}
    if pid is not None:
        kwargs.update(dict(project_id=pid))
    if model_type is not None:
        kwargs.update(dict(model_type=model_type))
    if save_to_catalog is not None:
        kwargs.update(dict(save_to_catalog=save_to_catalog))

    response = UserBlueprint.create(blueprint, **kwargs)
    assert response == UserBlueprint.from_server_data(mock_user_blueprint)
    assert response == UserBlueprint(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "POST"
    assert responses.calls[0].request.url == url

    # Inspect and verify the request
    body = json.loads(responses.calls[0].request.body.decode("utf-8").replace("'", '"'))
    expected = {
        "blueprint": blueprint,
        "decompressed_blueprint": True,
    }

    if expected_pid is not None:
        expected.update(dict(project_id=expected_pid))
    if expected_model_type is not None:
        expected.update(dict(model_type=expected_model_type))
    if expected_save_to_catalog is not None:
        expected.update(dict(save_to_catalog=expected_save_to_catalog))

    assert body == to_api(expected)


@responses.activate
@pytest.mark.parametrize("model_type, expected_model_type", [(None, None), ("foo", "foo")])
@pytest.mark.parametrize(
    "save_to_catalog, expected_save_to_catalog", [(None, True), (False, False)]
)
def test_create_blueprint_with_blueprint_id_and_project_id(
    make_url,
    mock_user_blueprint_with_project_id,
    blueprint_id,
    project_id,
    model_type,
    expected_model_type,
    save_to_catalog,
    expected_save_to_catalog,
):
    url = make_url("userBlueprints/fromBlueprintId/")
    responses.add(
        responses.POST,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mock_user_blueprint_with_project_id),
    )

    kwargs = {}
    if model_type is not None:
        kwargs.update(dict(model_type=model_type))
    if save_to_catalog is not None:
        kwargs.update(dict(save_to_catalog=save_to_catalog))

    response = UserBlueprint.clone_project_blueprint(blueprint_id, project_id, **kwargs)
    assert response == UserBlueprint.from_server_data(mock_user_blueprint_with_project_id)
    assert response == UserBlueprint(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "POST"
    assert responses.calls[0].request.url == url

    # Inspect and verify the request
    body = json.loads(responses.calls[0].request.body.decode("utf-8").replace("'", '"'))
    expected = {
        "blueprint_id": blueprint_id,
        "decompressed_blueprint": True,
        "project_id": project_id,
    }

    if expected_model_type is not None:
        expected.update(dict(model_type=expected_model_type))
    if expected_save_to_catalog is not None:
        expected.update(dict(save_to_catalog=expected_save_to_catalog))

    assert body == to_api(expected)


@responses.activate
@pytest.mark.parametrize("pid, expected_pid", [(None, None), ("foo", "foo")])
@pytest.mark.parametrize("model_type, expected_model_type", [(None, None), ("foo", "foo")])
@pytest.mark.parametrize(
    "save_to_catalog, expected_save_to_catalog", [(None, True), (False, False)]
)
def test_create_blueprint_with_user_blueprint_id(
    make_url,
    mock_user_blueprint,
    user_blueprint_id,
    pid,
    expected_pid,
    model_type,
    expected_model_type,
    save_to_catalog,
    expected_save_to_catalog,
):
    url = make_url("userBlueprints/fromUserBlueprintId/")
    responses.add(
        responses.POST,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mock_user_blueprint),
    )

    kwargs = {}
    if pid is not None:
        kwargs.update(dict(project_id=pid))
    if model_type is not None:
        kwargs.update(dict(model_type=model_type))
    if save_to_catalog is not None:
        kwargs.update(dict(save_to_catalog=save_to_catalog))

    response = UserBlueprint.clone_user_blueprint(user_blueprint_id, **kwargs)
    assert response == UserBlueprint.from_server_data(mock_user_blueprint)
    assert response == UserBlueprint(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "POST"
    assert responses.calls[0].request.url == url

    # Inspect and verify the request
    body = json.loads(responses.calls[0].request.body.decode("utf-8").replace("'", '"'))
    expected = {
        "user_blueprint_id": user_blueprint_id,
        "decompressed_blueprint": True,
    }

    if expected_pid is not None:
        expected.update(dict(project_id=expected_pid))
    if expected_model_type is not None:
        expected.update(dict(model_type=expected_model_type))
    if expected_save_to_catalog is not None:
        expected.update(dict(save_to_catalog=expected_save_to_catalog))

    assert body == to_api(expected)


@responses.activate
def test_update_blueprint_with_data(make_url, user_blueprint_id, mock_user_blueprint, blueprint):
    url = make_url("userBlueprints/{}/".format(user_blueprint_id))
    responses.add(
        responses.PATCH,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mock_user_blueprint),
    )
    response = UserBlueprint.update(blueprint, user_blueprint_id)
    assert response == UserBlueprint.from_server_data(mock_user_blueprint)
    assert response == UserBlueprint(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "PATCH"
    assert responses.calls[0].request.url == url


@responses.activate
def test_delete_blueprint_with_data(make_url, user_blueprint_id):
    url = make_url("userBlueprints/{}/".format(user_blueprint_id))
    responses.add(
        responses.DELETE, url, status=204, content_type="application/json",
    )
    UserBlueprint.delete(user_blueprint_id)
    assert responses.calls[0].request.method == "DELETE"
    assert responses.calls[0].request.url == url


@responses.activate
def test_add_to_project(
    make_url, project_id, user_blueprint_id, blueprint_id, mocked_add_to_menu_response,
):
    url = make_url("userBlueprintsProjectBlueprints/")
    responses.add(
        responses.POST,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mocked_add_to_menu_response),
    )

    response = UserBlueprint.add_to_project(
        project_id=project_id, user_blueprint_ids=[user_blueprint_id]
    )
    assert response == UserBlueprintAddToProjectMenu(**as_shallow_dict(response))
    assert len(response.added_to_menu) == 1
    assert response.added_to_menu[0].blueprint_id == blueprint_id
    assert response.added_to_menu[0].user_blueprint_id == user_blueprint_id
    assert responses.calls[0].request.method == "POST"
    assert responses.calls[0].request.url == url


@responses.activate
def test_get_input_types(
    make_url, project_id, user_blueprint_id, blueprint_id, mocked_input_types,
):
    url = make_url("userBlueprintsInputTypes/")
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mocked_input_types),
    )

    response = UserBlueprint.get_input_types()
    assert response == UserBlueprintAvailableInput.from_server_data(mocked_input_types)
    assert response == UserBlueprintAvailableInput(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "GET"
    assert responses.calls[0].request.url == url


@responses.activate
def test_get_available_tasks(
    make_url, project_id, user_blueprint_id, blueprint_id, mocked_available_tasks,
):
    url = make_url("userBlueprintsTasks/")
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mocked_available_tasks),
    )

    response = UserBlueprint.get_available_tasks()
    assert response.tasks[0].task_definition.url.documentation == (
        "/model-docs/tasks/ABC-Adaboost-Classifier.html"
    )
    assert response == UserBlueprintAvailableTasks.from_server_data(mocked_available_tasks)
    assert response == UserBlueprintAvailableTasks(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "GET"
    assert responses.calls[0].request.url == url


@responses.activate
def test_validate_task_parameters(
    make_url, project_id, user_blueprint_id, blueprint_id, mocked_validated_task_parameters,
):
    url = make_url("userBlueprintsTaskParameters/")
    responses.add(
        responses.POST,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(mocked_validated_task_parameters),
    )

    response = UserBlueprint.validate_task_parameters(
        output_method="P",
        task_code="KERASC",
        task_parameters=[{"paramName": "learning_rate", "newValue": "abc"}],
    )
    assert response == (
        UserBlueprintValidateTaskParameters.from_server_data(mocked_validated_task_parameters)
    )
    assert response == UserBlueprintValidateTaskParameters(**as_shallow_dict(response))
    assert responses.calls[0].request.method == "POST"
    assert responses.calls[0].request.url == url


@pytest.mark.parametrize("limit", [0, 10])
@responses.activate
def test_retrieve_shared_roles(make_url, user_blueprint_id, mock_roles_response, limit):
    original_limit = limit
    if limit == 0:
        limit = DEFAULT_BATCH_SIZE
    urlA = make_url("userBlueprints/{}/sharedRoles/?offset=3&limit={}").format(
        user_blueprint_id, limit
    )
    urlB = make_url("userBlueprints/{}/sharedRoles/?limit={}&offset=3").format(
        user_blueprint_id, limit
    )
    responses.add(
        responses.GET,
        urlA,
        status=200,
        content_type="application/json",
        body=json.dumps(mock_roles_response),
    )
    response = UserBlueprint.list_shared_roles(user_blueprint_id, limit=original_limit, offset=3)
    assert response == (
        UserBlueprintSharingListController.from_server_data(mock_roles_response).data
    )
    assert response == UserBlueprintSharingListController(data=response).data
    assert responses.calls[0].request.method == "GET"
    assert responses.calls[0].request.url in [urlA, urlB]


@pytest.mark.parametrize("recipientType", ["user", "group", "organization"])
@pytest.mark.parametrize("role", ["CONSUMER", "EDITOR", "OWNER"])
@responses.activate
def test_update_shared_roles(make_url, user_blueprint_id, role, recipientType):
    url = make_url("userBlueprints/{}/sharedRoles/".format(user_blueprint_id))
    responses.add(
        responses.PATCH, url, status=204, content_type="application/json",
    )
    response = UserBlueprint.update_shared_roles(
        user_blueprint_id, [GrantAccessControlWithUsernameValidator(role, recipientType, "test")]
    )
    assert response.status_code == 204
    assert responses.calls[0].request.method == "PATCH"
    assert responses.calls[0].request.url == url


@responses.activate
def test_catalog_search(make_url):
    url = make_url("catalogItems/")
    responses.add(
        responses.GET,
        url,
        status=200,
        content_type="application/json",
        body=json.dumps(
            {
                "data": [
                    to_api(
                        dict(
                            id="a",
                            catalog_name="b",
                            info_creator_full_name="c",
                            user_blueprint_id="d",
                            description="e",
                            last_modifier_name="f",
                        )
                    )
                ]
            }
        ),
    )
    response = UserBlueprint.search_catalog()
    assert response == [
        UserBlueprintCatalogSearch(
            id="a",
            catalog_name="b",
            info_creator_full_name="c",
            user_blueprint_id="d",
            description="e",
            last_modifier_name="f",
        )
    ]
    assert responses.calls[0].response.status_code == 200
    assert responses.calls[0].request.method == "GET"
    request_url = responses.calls[0].request.url
    parsed_url = urllibparse.urlparse(request_url)
    qs = urllibparse.parse_qs(parsed_url.query)
    assert qs == dict(limit=["100"], offset=["0"], orderBy=["-created"], type=["user_blueprint"])

    response = UserBlueprint.search_catalog(
        search="foo",
        tag="a,b,c",
        limit=10,
        offset=5,
        owner_user_id="test_id",
        owner_username="test_name",
        order_by="relevance",
    )
    assert response == [
        UserBlueprintCatalogSearch(
            id="a",
            catalog_name="b",
            info_creator_full_name="c",
            user_blueprint_id="d",
            description="e",
            last_modifier_name="f",
        )
    ]
    assert responses.calls[1].response.status_code == 200
    assert responses.calls[1].request.method == "GET"
    request_url = responses.calls[1].request.url
    parsed_url = urllibparse.urlparse(request_url)
    qs = urllibparse.parse_qs(parsed_url.query)
    assert qs == dict(
        limit=["10"],
        offset=["5"],
        orderBy=["relevance"],
        ownerUserId=["test_id"],
        ownerUsername=["test_name"],
        searchFor=["foo"],
        tag=["a,b,c"],
        type=["user_blueprint"],
    )

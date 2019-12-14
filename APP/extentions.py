from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

shitBuilder = {
    'code': 200,
    'message': "",
    'result':
        {
            'username': "admin",
            'avatar': "https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png",
            'createTime': 1497160610259,
            'creatorId': 'admin',
            'deleted': 0,
            'id': "0001",
            'lang': "zh-CN",
            'lastLoginIp': "27.154.74.117",
            'lastLoginTime': 1534837621348,
            'name': "baibai",
            'password': "",
            'roleId': "admin",
            'status': 1,
            'telephone': "",
            'token': "4291d7da9005377ec9aec4a71ea837f",
            'timestamp': 1576246189302,
        },
    '_headers':
        {
            'Custom-Header': "0001",
            '_status': 200
        }
}
shits = {
    'code': 200,
    'message': "",
    'result':
        {
            'avatar': '/avatar2.jpg',
            'createTime': 1497160610259,
            'creatorId': 'admin',
            'deleted': 0,
            'id': '4291d7da9005377ec9aec4a71ea837f',
            'lastLoginIp': '27.154.74.117',
            'lastLoginTime': 1534837621348,
            'merchantCode': 'TLif2btpzg079h15bk',
            'name': 'admin',
            'password': '',
            'role': {
                'createTime': 1497160610259,
                'creatorId': 'system',
                'deleted': 0,
                'describe': '拥有所有权限',
                'id': 'admin',
                'name': '管理员',
                'permissions': [
                    {
                        'roleId': 'admin',
                        'permissionId': 'dashboard',
                        'permissionName': '仪表盘',
                        'actions':
                            [
                                {
                                    "action": "add",
                                    "defaultCheck": False,
                                    "describe": "新增"
                                },
                                {
                                    "action": "query",
                                    "defaultCheck": False,
                                    "describe": "查询"
                                },
                                {"action": "get",
                                 "defaultCheck": False,
                                 "describe": "详情"
                                 },
                                {
                                    "action": "update",
                                    "defaultCheck": False,
                                    "describe": "修改"
                                },
                                {
                                    "action": "delete",
                                    "defaultCheck": False,
                                    "describe": "删除"
                                }
                            ],
                        'actionEntitySet': [
                            {
                                'action': 'add',
                                'describe': '新增',
                                'defaultCheck': False
                            },
                            {
                                'action': 'query',
                                'describe': '查询',
                                'defaultCheck': False
                            },
                            {
                                'action': 'get',
                                'describe': '详情',
                                'defaultCheck': False
                            },
                            {
                                'action': 'update',
                                'describe': '修改',
                                'defaultCheck': False
                            },
                            {
                                'action': 'delete',
                                'describe': '删除',
                                'defaultCheck': False
                            }
                        ],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'exception',
                        'permissionName': '异常页面权限',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "query",
                                "defaultCheck": False,
                                "describe": "查询"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [
                            {
                                'action': 'add',
                                'describe': '新增',
                                'defaultCheck': False
                            },
                            {
                                'action': 'query',
                                'describe': '查询',
                                'defaultCheck': False
                            }, {
                                'action': 'get',
                                'describe': '详情',
                                'defaultCheck': False
                            }, {
                                'action': 'update',
                                'describe': '修改',
                                'defaultCheck': False
                            }, {
                                'action': 'delete',
                                'describe': '删除',
                                'defaultCheck': False
                            }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'result',
                        'permissionName': '结果权限',
                        'actions': [
                            {"action": "add",
                             "defaultCheck": False,
                             "describe": "新增"
                             },
                            {
                                "action": "query",
                                "defaultCheck": False,
                                "describe": "查询"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'query',
                            'describe': '查询',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'profile',
                        'permissionName': '详细页权限',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "query",
                                "defaultCheck": False,
                                "describe": "查询"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'query',
                            'describe': '查询',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'table',
                        'permissionName': '表格权限',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "import",
                                "defaultCheck": False,
                                "describe": "导入"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'import',
                            'describe': '导入',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'form',
                        'permissionName': '表单权限',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "query",
                                "defaultCheck": False,
                                "describe": "查询"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'query',
                            'describe': '查询',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'order',
                        'permissionName': '订单管理',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "query",
                                "defaultCheck": False,
                                "describe": "查询"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'query',
                            'describe': '查询',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'permission',
                        'permissionName': '权限管理',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'role',
                        'permissionName': '角色管理',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'table',
                        'permissionName': '桌子管理',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "query",
                                "defaultCheck": False,
                                "describe": "查询"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'query',
                            'describe': '查询',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    },
                    {
                        'roleId': 'admin',
                        'permissionId': 'user',
                        'permissionName': '用户管理',
                        'actions': [
                            {
                                "action": "add",
                                "defaultCheck": False,
                                "describe": "新增"
                            },
                            {
                                "action": "import",
                                "defaultCheck": False,
                                "describe": "导入"
                            },
                            {
                                "action": "get",
                                "defaultCheck": False,
                                "describe": "详情"
                            },
                            {
                                "action": "update",
                                "defaultCheck": False,
                                "describe": "修改"
                            },
                            {
                                "action": "delete",
                                "defaultCheck": False,
                                "describe": "删除"
                            },
                            {
                                "action": "export",
                                "defaultCheck": False,
                                "describe": "导出"
                            }
                        ],
                        'actionEntitySet': [{
                            'action': 'add',
                            'describe': '新增',
                            'defaultCheck': False
                        }, {
                            'action': 'import',
                            'describe': '导入',
                            'defaultCheck': False
                        }, {
                            'action': 'get',
                            'describe': '详情',
                            'defaultCheck': False
                        }, {
                            'action': 'update',
                            'describe': '修改',
                            'defaultCheck': False
                        }, {
                            'action': 'delete',
                            'describe': '删除',
                            'defaultCheck': False
                        }, {
                            'action': 'export',
                            'describe': '导出',
                            'defaultCheck': False
                        }],
                        'actionList': None,
                        'dataAccess': None
                    }
                ],
                'status': 1
            }
        }
}


def init_extentions(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    Bootstrap(app)
    # DebugToolbarExtension(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    moment = Moment()
    csrf = CSRFProtect()



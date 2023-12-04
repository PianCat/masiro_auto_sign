def sendMessage(title: str, content: str, type: str):
    """
    整合消息
    :param title: 标题
    :param content: 内容
    :param type: 类型
    :return: none
    """
    if (skyland_notify):
        type = type.strip()
        if type == 'TG':
            notify.telegram_bot(title, content)
        elif type == 'BARK':
            notify.bark(title, content)
        elif type == 'DD':
            notify.dingding_bot(title, content)
        elif type == 'FSKEY':
            notify.feishu_bot(title, content)
        elif type == 'GOBOT':
            notify.go_cqhttp(title, content)
        elif type == 'GOTIFY':
            notify.gotify(title, content)
        elif type == 'IGOT':
            notify.iGot(title, content)
        elif type == 'SERVERJ':
            notify.serverJ(title, content)
        elif type == 'PUSHDEER':
            notify.pushdeer(title, content)
        elif type == 'PUSHPLUS':
            notify.pushplus_bot(title, content)
        elif type == 'QMSG':
            notify.qmsg_bot(title, content)
        elif type == 'QYWXAPP':
            notify.wecom_app(title, content)
        elif type == 'QYWXBOT':
            notify.wecom_bot(title, content)
        else:
            pass

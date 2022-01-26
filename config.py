class Config(object):
    # scheduler configs
    SCHEDULER_API_ENABLED = True
    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 5}}

    # backround checker config
    CHECKER_DELAY = 10
    CHECKER_NODE = 'http://127.0.0.1:8545'

    # Contracts
    # AvalonInfoFacade
    INFO_FACADE = '0x8D81A3DCd17030cD5F23Ac7370e4Efb10D2b3cA4'
    # AvalonVaultSaver
    VAULT_SAVER = '0x0aec7c174554AF8aEc3680BB58431F6618311510'

    # private key of saving bot
    PK = '0xa90358bce43846d107958470c772a5f37778668bdb6663f8026a972f163886a3'

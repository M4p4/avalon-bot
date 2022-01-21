class Config(object):
    #scheduler configs
    SCHEDULER_API_ENABLED = True
    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 5}}

    #backround checker config
    CHECKER_DELAY = 10
    CHECKER_NODE = 'http://localhost:8545'

    #Contracts
    #AvalonInfoFacade
    INFO_FACADE = ''
    #AvalonVaultSaver
    VAULT_SAVER = ''

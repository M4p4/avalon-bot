class Config(object):
    #scheduler configs
    SCHEDULER_API_ENABLED = True
    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 5}}

    #backround checker config
    CHECKER_DELAY = 10
    CHECKER_NODE = 'http://localhost:8545'

    #Contracts
    #AvalonInfoFacade
    INFO_FACADE = '0x49fd2BE640DB2910c2fAb69bB8531Ab6E76127ff'
    #AvalonVaultSaver
    VAULT_SAVER = '0x5c74c94173F05dA1720953407cbb920F3DF9f887'

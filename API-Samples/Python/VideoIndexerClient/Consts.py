from dataclasses import dataclass


@dataclass
class Consts:
    ApiVersion: str
    ApiEndpoint: str
    AzureResourceManager: str
    AccountName: str
    ResourceGroup: str
    DeploymentName: str
    SubscriptionId: str

    def __post_init__(self):
        if self.AccountName is None or self.AccountName == '' \
            or self.ResourceGroup is None or self.ResourceGroup == '' \
            or self.SubscriptionId is None or self.SubscriptionId == '' \
            or self.DeploymentName is None or self.DeploymentName == '':
            raise ValueError('Please Fill In SubscriptionId, Account Name and Resource Group on the Constant Class!')
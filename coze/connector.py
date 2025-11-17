from cozepy import COZE_CN_BASE_URL, Coze, TokenAuth


class Connector:
    # def __init__(self):
    #     self.coze_api_token = self._load_key()
    #
    # def _load_key(self):
    #     with open("coze_key", 'r') as f:
    #         return f.read()

    def run(self, coze_api_token, workflow_id):
        # Get an access_token through personal access token or oauth.
        # coze_api_token = 'cztei_qf3mP8SdjEx3qdD23yQbLr08g0sA5n1t5hXTIP61n1VtYrsS5fql7RhsSne2OCw8o'
        # The default access is api.coze.com, but if you need to access api.coze.cn,
        # please use base_url to configure the api endpoint to access
        coze_api_base = COZE_CN_BASE_URL

        from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  # noqa

        # Init the Coze client through the access_token.
        coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

        # Create a workflow instance in Coze, copy the last number from the web link as the workflow's ID.
        # workflow_id = '7572232345110282266'

        # Call the coze.workflows.runs.create method to create a workflow run. The create method
        # is a non-streaming chat and will return a WorkflowRunResult class.
        workflow = coze.workflows.runs.create(
            workflow_id=workflow_id,
            parameters={
                "input": "Call of Duty: Black Ops 7"
            }
        )

        print("workflow.data", workflow.data)


if __name__ == '__main__':
    Connector().run()

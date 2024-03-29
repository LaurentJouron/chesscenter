class BaseController:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def action(self):
        """
        Define the action for the controller.

        Raises:
            NotImplementedError: This method should be implemented in
            subclasses.

        Returns:
            None
        """
        raise NotImplementedError

    def run(self):
        """
        Run the controller's action.

        Returns:
            None
        """
        return self.action()

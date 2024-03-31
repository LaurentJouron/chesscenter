from .controllers.home_controllers import HomeController
from chesscenter.views.home_views import HomeView

view = HomeView()


def run_application():
    controller = HomeController()
    while controller is not None:
        next_controller = controller.run()
        controller = next_controller
    view.good_by()


run_application()

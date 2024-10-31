from pypeerman.endpoints import PeeringEndpoint


class Messaging:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.contact_assignments = PeeringEndpoint(
            pm_instance, resource_name, "contact-assignments"
        )
        self.contact_roles = PeeringEndpoint(
            pm_instance, resource_name, "contact-roles"
        )
        self.contacts = PeeringEndpoint(pm_instance, resource_name, "contacts")
        self.emails = PeeringEndpoint(pm_instance, resource_name, "emails")

from pypeerman.endpoints import PeeringEndpoint


class Extras:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.config_context_assignments = PeeringEndpoint(
            pm_instance, resource_name, "config-context-assignments"
        )
        self.config_contexts = PeeringEndpoint(
            pm_instance, resource_name, "config-contexts"
        )
        self.export_templates = PeeringEndpoint(
            pm_instance, resource_name, "export-templates"
        )
        self.ix_api = PeeringEndpoint(pm_instance, resource_name, "ix_api")
        self.object_changes = PeeringEndpoint(
            pm_instance, resource_name, "object-changes"
        )
        self.tags = PeeringEndpoint(pm_instance, resource_name, "tags")
        self.webhooks = PeeringEndpoint(pm_instance, resource_name, "webhooks")

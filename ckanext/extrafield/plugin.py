import ckan.plugins as p
import ckan.plugins.toolkit as tk
#from ckan.plugins.toolkit import Invalid


class ExtraFieldPlugin(p.SingletonPlugin,tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    # IConfigurer

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')
        tk.add_resource('fanstatic', 'extrafield')

    def _modify_package_schema(self, schema):
        schema.update({
            'anzlic_id': [tk.get_validator('ignore_missing'),tk.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        schema = super(ExtraFieldPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExtraFieldPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExtraFieldPlugin, self).show_package_schema()
        schema.update({
            'anzlic_id': [tk.get_converter('convert_from_extras'),tk.get_validator('ignore_missing')]
        })
        return schema

#    def anzlic_validation(value):
#        if not vlaue.startswith('ANZ...'):
#            raise Invalid("Doesn't start with ANZ...")
#        if not value.len() == 15:
#            raise Invalid("Should be 15 characters long")
#        return value

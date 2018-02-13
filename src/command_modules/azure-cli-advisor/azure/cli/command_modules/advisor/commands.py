# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.command_modules.advisor._client_factory import \
    (advisor_mgmt_client_factory,
     recommendations_mgmt_client_factory,
     configurations_mgmt_client_factory)


def load_command_table(self, _):
    from azure.cli.core.commands import CliCommandType
    advisor_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.advisor.custom#{}')

    with self.command_group('advisor recommendation') as g:
        g.custom_command('list', 'cli_advisor_list_recommendations',
                         client_factory=recommendations_mgmt_client_factory)
        g.custom_command('disable', 'cli_advisor_disable_recommendations',
                         client_factory=advisor_mgmt_client_factory)
        g.custom_command('enable', 'cli_advisor_enable_recommendations',
                         client_factory=advisor_mgmt_client_factory)

    with self.command_group('advisor configuration', client_factory=configurations_mgmt_client_factory) as g:
        g.custom_command('list', 'cli_advisor_list_configurations')
        g.custom_command('show', 'cli_advisor_show_configuration')
        g.generic_update_command('update',
                                 getter_name='cli_advisor_show_configuration',
                                 getter_type=advisor_custom,
                                 setter_name='_cli_advisor_set_configuration',
                                 setter_type=advisor_custom,
                                 custom_func_name='cli_advisor_update_configurations',
                                 custom_func_type=advisor_custom)

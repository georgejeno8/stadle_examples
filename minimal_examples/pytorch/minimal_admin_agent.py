from stadle import AdminAgent
from stadle.lib.util import client_arg_parser
from stadle.lib.entity.model import BaseModel
from stadle import BaseModelConvFormat

from minimal_model import MinimalModel

def get_minimal_model():
    return BaseModel("PyTorch-Minimal-Model", MinimalModel(), BaseModelConvFormat.pytorch_format)


if __name__ == '__main__':
    args = client_arg_parser()

    admin_agent = AdminAgent(config_file=args.config_path, simulation_flag=args.simulation,
                             comm_protocol=args.comm_protocol, aggregator_ip_address=args.aggregator_ip, reg_port=args.reg_port,
                             exch_port=args.exch_port, model_path=args.model_path, base_model=get_minimal_model(),
                             agent_running=args.agent_running)

    admin_agent.preload()
    admin_agent.initialize()

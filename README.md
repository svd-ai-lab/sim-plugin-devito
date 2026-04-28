# sim-plugin-devito

Devito driver for [sim-cli](https://github.com/svd-ai-lab/sim-cli),
distributed as an out-of-tree plugin.

Devito driver for sim.

## Install

```bash
sim plugin install devito
```

Other paths:

```bash
pip install git+https://github.com/svd-ai-lab/sim-plugin-devito@v0.1.0
pip install https://github.com/svd-ai-lab/sim-plugin-devito/releases/download/v0.1.0/sim_plugin_devito-0.1.0-py3-none-any.whl
pip install -e .
```

After install:

```bash
sim plugin doctor devito
sim plugin sync-skills
```

## Development

```bash
git clone https://github.com/svd-ai-lab/sim-plugin-devito
cd sim-plugin-devito
uv sync
uv run pytest
```

## License

Apache-2.0.

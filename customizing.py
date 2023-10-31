from traitlets.config.manager import BaseJSONConfigManager
from pathlib import Path
path = Path.home() / ".jupyter" / "nbconfig"
cm = BaseJSONConfigManager(config_dir=str(path))
cm.update(
    "rise",
    {
        "backimage": "bg.jpg",
        "enable_chalkboard": True
     }
)

cm.update('livereveal', {
        'width': 1024,
        'height': 768,
        'scroll': True,
})
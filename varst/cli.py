from typing import Optional
from typing import Sequence

from varst import application


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Main function to run application

        Args:
            argv: Arguments vector

    """
    app = application.Application()
    app.run(argv)

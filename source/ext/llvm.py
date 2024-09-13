from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

# class LLVMPullRequest(SphinxRole):
#     pass


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("llvm-pr", LLVMPullRequest)

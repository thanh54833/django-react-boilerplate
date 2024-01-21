# Create your tests here.
from backend.product.models import Snippet

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

#
# snippet = Snippet(code='print("hello, world")\n')
# snippet.save()

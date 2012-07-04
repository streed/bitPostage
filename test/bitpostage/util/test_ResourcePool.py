import inject
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from bitpostage.util.ResourcePool import ResourcePool
from Queue import Empty

@raises( Empty )
def test_ResourcePool_raises_Empty_exception():
	"""ResourcePool should raise a Empty exception when nothing is left in the pool"""

	injector = inject.Injector()
	inject.register( injector )
	injector.bind( "resourcePoolTimeout", to=0 )
	injector.bind( "maxObjects", to=2 )

	resourcePool = ResourcePool()

	with resourcePool as w:
		with resourcePool as w1:
			with resourcePool as w2:
				pass

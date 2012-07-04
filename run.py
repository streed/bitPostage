import inject
from bitpostage.ModuleConfig import ModuleConfig
from bitpostage.BitPostageServer import BitPostageApplication

def main():
	bitpostageApp = BitPostageApplication()

if __name__ == "__main__":
	injector = inject.Injector()
	moduleConfig = ModuleConfig()
	moduleConfig( injector )
	inject.register( injector )
	main()

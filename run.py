import inject
from ModuleConfig import ModuleConfig
from BitPostageServer import BitPostageApplication

def main():
	bitpostageApp = BitPostageApplication()

if __name__ == "__main__":
	injector = inject.Injector()
	moduleConfig = ModuleConfig()
	moduleConfig( injector )
	inject.register( injector )
	main()

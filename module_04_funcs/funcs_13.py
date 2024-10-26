from platform import platform, machine, processor, system, version
print(platform())
print(platform(aliased=True))
print(platform(aliased=False, terse=True))
print(machine())
print(processor())
print(system())
print(version())
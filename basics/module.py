# eigen module/ dateien
from concepts import quadrat

print(quadrat(8))

# vorinstallierte module
from platform import platform

print(platform())

# module aus dem package manager
import wikipedia

result = wikipedia.page("Wikipedia")
print(result.summary)

# PIP: package manager for packages/modules
# module is ready code
# benefits: contain a set of functions you might use in your app
# if modules are not built in just download using: pip install packagename
# install camelcase
# to use a package, just call to it using import keyword
import camelcase

c = camelcase.CamelCase()
text = "francis mung'ang'u"
print(c.hump(text))
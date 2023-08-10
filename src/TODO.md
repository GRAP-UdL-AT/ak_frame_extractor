https://test.pypi.org/project/ak-frame-extractor/

https://pypi.org/project/ak-video-analyser/
https://packaging.python.org/en/latest/tutorials/packaging-projects/


py -m twine upload --repository testpypi dist/


Preparing packages
---------------------
py -m pip install --upgrade build
py -m build

Testing package and upload packages
---------------------
## Testing Pypi.org
py -m pip install --upgrade twine
twine upload --repository testpypi ./dist/*

## Final repo Pypi.org
twine upload ./dist/* --verbose

URL: https://test.pypi.org/project/ak-frame-extractor/



Solving dependences conflicts
-----------------------------
pip install -i https://test.pypi.org/simple/ ak-frame-extractor
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ak-frame-extractor

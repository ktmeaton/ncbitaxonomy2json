[![GitHub (pre-)release](https://img.shields.io/badge/Release-v0.3.1-red.svg)](https://github.com/ktmeaton/NCBImeta/releases/tag/v0.3.1)
[![GitHub license](https://img.shields.io/github/license/ktmeaton/NCBImeta.svg?style=flat)](https://github.com/ktmeaton/NCBImeta/blob/master/LICENSE)




# ncbitaxonomy2json
Converts the NCBI taxidlineage.dmp file into JSON format.


## Version

Stable - Version v0.0.1 (master)

## Python Requirements
Python 2.6+ or 3.4+
Module anytree

```
pip install --user anytree
```

## Installation

git clone https://github.com/ktmeaton/ncbitaxonomy2json.git
cd ncbitaxonomy2json 

## Usage

### Convert the taxidlineage.dmp file into json format and write to output file
```
python ncbitaxonomy2json.py --input example/taxidlineage.dmp --output example/taxidlineage.json
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

See CHANGELOG.md.

## Credits

author: Katherine Eaton (ktmeaton@gmail.com)

## License

TODO: Write license

## Helpful commands  
Merging a development branch into master:  
        (on branch development)$ git merge master  
        (resolve any merge conflicts if there are any)  
        git checkout master  
        git merge --no-ff development (there won't be any conflicts now)  
        
## About

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

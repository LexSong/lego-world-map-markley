# [![](docs/worldmap.png)](https://lexsong.github.io/lego-world-map-markley/)
# [LEGO World Map in Markley’s Projection](https://lexsong.github.io/lego-world-map-markley/)

### How to build the website

    jupytext worldmap.py --to ipynb
    jupyter nbconvert --execute worldmap.ipynb --to html --output docs/index.html

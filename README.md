# Explorations in Texture Learning

This is the code repository for the work *Explorations in Texture Learning* in ICLR 2024, Tiny Papers track LINK 

To reproduce the results in this paper, simply run `python3 main.py` in your terminal. This will download the DTD dataset, fetch the pretrained ImageNet model, and run the texture learning analysis. When the program completes, the results will be contained in `texture_object_top3.csv`. With this csv file, you can create tables for the texture-object associations like this:

|texture class|imagenet class top 1|effect size top 1|imagenet class top 2|effect size top 2|imagenet class top 3|effect size top 3|
|---|---|---|---|---|---|---|
|honeycombed|honeycomb|0.7627119|chain_mail|0.050847456|leaf_beetle|0.016949153|
|cobwebbed|spider_web|0.6615385|barn_spider|0.06153846|radio_telescope|0.03076923|
|waffled|waffle_iron|0.44705883|honeycomb|0.105882354|pretzel|0.07058824|
|knitted|dishrag|0.36956522|wool|0.26086956|cardigan|0.1521739|
|striped|zebra|0.35714287|tiger|0.16666667|velvet|0.11904762|
|spiralled|coil|0.32323232|maze|0.060606062|knot|0.04040404|
|bubbly|bubble|0.32038835|beer_glass|0.097087376|honeycomb|0.058252428|
|stratified|cliff|0.27083334|velvet|0.1875|stone_wall|0.09375|
|polka-dotted|bib|0.23762377|Windsor_tie|0.12871288|shower_curtain|0.10891089|
|dotted|bib|0.23762377|shower_curtain|0.12871288|wallet|0.10891089|
|wrinkled|velvet|0.21153846|quilt|0.17307693|wool|0.057692308|
|grid|window_screen|0.19626169|oscilloscope|0.11214953|shoji|0.07476635|
|woven|hamper|0.19626169|velvet|0.12149533|dishrag|0.093457945|
|stained|velvet|0.19298245|potpie|0.03508772|handkerchief|0.02631579|
|paisley|velvet|0.1923077|wool|0.115384616|shower_curtain|0.10576923|
|lacelike|handkerchief|0.1904762|velvet|0.104761906|stole|0.104761906|
|frilly|head_cabbage|0.1875|hoopskirt|0.09821428|velvet|0.08035714|
|perforated|strainer|0.18691589|space_heater|0.07476635|honeycomb|0.06542056|
|zigzagged|maze|0.17431192|envelope|0.12844037|quilt|0.110091746|
|meshed|window_screen|0.16216215|chainlink_fence|0.14414415|honeycomb|0.117117114|
|gauzy|shower_curtain|0.16071428|velvet|0.09821428|window_shade|0.071428575|
|crystalline|plastic_bag|0.16071428|honeycomb|0.09821428|pinwheel|0.071428575|
|braided|knot|0.16037735|hamper|0.11320755|dishrag|0.08490566|
|flecked|wool|0.15517241|velvet|0.0862069|cardigan|0.06896552|
|cracked|stone_wall|0.15178572|guillotine|0.0625|honeycomb|0.05357143|
|blotchy|velvet|0.1491228|ant|0.05263158|shower_curtain|0.02631579|
|banded|shower_curtain|0.14018692|web_site|0.093457945|Windsor_tie|0.07476635|
|matted|wool|0.13913043|komondor|0.07826087|wig|0.052173913|
|interlaced|maze|0.13392857|prayer_rug|0.08928572|buckle|0.08035714|
|chequered|wool|0.13274336|tray|0.097345136|web_site|0.07079646|
|veined|leaf_beetle|0.13157895|head_cabbage|0.096491225|walking_stick|0.05263158|
|pleated|window_shade|0.13043478|shower_curtain|0.12173913|velvet|0.11304348|
|lined|shower_curtain|0.11504425|wool|0.07964602|window_shade|0.07964602|
|crosshatched|window_screen|0.11504425|handkerchief|0.061946902|velvet|0.053097345|
|grooved|radiator|0.114035085|velvet|0.096491225|doormat|0.078947365|
|fibrous|hay|0.11304348|wool|0.052173913|pot|0.052173913|
|swirly|velvet|0.112068966|fire_screen|0.112068966|shower_curtain|0.094827585|
|scaly|honeycomb|0.112068966|velvet|0.060344826|tile_roof|0.060344826|
|freckled|lipstick|0.10810811|seat_belt|0.072072074|Band_Aid|0.072072074|
|studded|strainer|0.10526316|Windsor_tie|0.0877193|cuirass|0.07017544|
|marbled|velvet|0.097345136|cliff|0.053097345|spider_web|0.044247787|
|bumpy|custard_apple|0.09243698|jackfruit|0.05042017|abacus|0.033613447|
|potholed|geyser|0.09174312|volcano|0.08256881|manhole_cover|0.055045873|
|sprinkled|ice_cream|0.08547009|dough|0.05982906|confectionery|0.042735044|
|porous|French_loaf|0.078947365|velvet|0.05263158|honeycomb|0.05263158|
|pitted|pomegranate|0.06837607|doormat|0.051282052|velvet|0.051282052|
|smeared|mask|0.05982906|velvet|0.051282052|paintbrush|0.042735044|

By default, the csv will contain the top 3 texture-object associations for each texture class. To change this number, run `python3 main.py --maxk k` with your desired value for k instead. 

If running on a CPU, this may take some time (~20 minutes). If running on a GPU, the Dockerfile provided can be used to setup the environment with the proper packages installed. 

To cite the paper:

```
bibtex
```

**Acknowledgements**:
This material is based upon work supported by, or in part by, the National Science Foundation under Grant No. CNS1946022 and Grant No. CNS2343611. Any opinions, findings, and conclusions or recommendations expressed in this publication are those of the author(s) and do not necessarily reflect the views of the National Science Foundation, or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for government purposes notwithstanding any copyright notation hereon.
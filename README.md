scrape content and find key sentences
=====================================

the `create_content.sh` script runs this like of hacks to a) scrape
all the management-related posts from [Larson's
blog](https://lethain.com), and b) runs the
[TextRank](https://github.com/summanlp/textrank) algorithm on them, to
extract the most "meaningful" sentences from each blog post.  It then
spits out these sentences, along with a link to the post, in a format
you can paste in to the incredible [Cheap Bots Done
Quick](https://cheapbotsdonequick.com/).

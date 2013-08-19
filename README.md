Example of using word2vec
===========

A common test of language competence is to identify a word which doesn't belong in a list with several other words. 

As an example, in the list: car, boat, plane, train, microwave, all the words except microwave are modes of transportation, so the answer would be microwave.

Until recently, such a task would have been nearly impossible for a computer to solve without extreme effort on behalf of the programmer. A tool called word2vec [https://code.google.com/p/word2vec/] was released a few days ago, which allows for efficient computation of distributed representations of words as real-valued vectors. Feature vectors are learned by using recent advances in deep learning and neural networks, and have been shown to learn very rich representations of word meaning and usage. See this paper for more information on how the vector representations are learned: http://arxiv.org/pdf/1301.3781.pdf

With this new tool, it is possible to examine a range of previously difficult NLP tasks, one of which is identifying a word which doesn't belong in a list. This program demonstrates this capability. Some samples:

->staple hammer saw drill

I think staple doesnt belong in this list!

->math shopping reading science

I think shopping doesnt belong in this list!

->rain snow sleet sun

I think sun doesnt belong in this list!

->eight six seven five three owe nine

I think owe doesnt belong in this list!

->breakfast cereal dinner lunch

I think cereal doesnt belong in this list!

->england spain france italy greece germany portugal australia

I think australia doesnt belong in this list!

etc.

The vector representations were learned from 1GB of wikipedia text, which if I remember correctly amounted to about 100-200 million words. If you're looking to download and try it out, the file which holds the vectors is pretty large - about 500M. I chunked it up into smaller files so that GitHub would let me push.

If you decide to try it out, keep in mind that the longer the list, the better it will perform.
Feel free to check it out, pull, modify, anything. word2vec is really an amazing tool which has the potential to make our NLP systems incredibly more intelligent!

If you want to see some visualizations of the representations, see the /visualizations directory. t-SNE was used to generate the 2D scatterplot.

import sam_caption_metrics.pycocoevalcap.meteor.meteor

hypo = ['this is the model generated sentence1 which seems good enough']
ref = ['this is one reference sentence for sentence1',
        'this is a reference sentence for sentence2 which was generated by your model']

m = meteor.Meteor()

score = m._score(hypo[0], ref)
print(score)

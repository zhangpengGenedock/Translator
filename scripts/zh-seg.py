

if __name__ == '__main__':
    import thulac
    thu1 = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
    thu1.cut_f("data/train_10000_before_seg.zh", "data/train_10000.zh")


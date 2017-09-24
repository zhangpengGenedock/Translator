

if __name__ == '__main__':
    import thulac
    thu1 = thulac.thulac(seg_only=True) 
    thu1.fast_cut_f("../data/dev.zh", "../actual_data/dev_seg.zh")


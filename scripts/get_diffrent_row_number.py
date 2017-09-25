
if __name__ == '__main__':
        with open('../stf_data/train_ctb_seg.zh') as f1, open('../stf_data/train.zh') as f2:
            for i, (line1, line2) in enumerate(zip(f1, f2)):
                #if "".join(line1.split()) != "".join(line2.split()):
                if line1.strip()[0] != line2.strip()[0]:
                    print i
                    break

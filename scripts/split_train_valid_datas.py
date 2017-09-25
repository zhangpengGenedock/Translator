from sklearn.cross_validation import train_test_split

if __name__ == '__main__':
    with open('../stf_data/train.en') as f1, open('../stf_data/train_ctb_seg.zh') as f2, open(
            '../stf_data/train_split.en', 'w') as f3, open('../stf_data/train_split.zh', 'w') as f4, open(
            '../stf_data/test_split.en', 'w') as f5, open('../stf_data/test_split.zh', 'w') as f6:
        # with open('../data/dev.en') as f1, open('../data/dev.zh') as f2, open('../data/train_split.en', 'w') as f3, open('../data/train_split.zh', 'w') as f4, open('../data/test_split.en', 'w') as f5, open('../data/test_split.zh', 'w') as f6:
        X = f1.readlines()
        y = f2.readlines()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)
        f3.writelines(["%s\n" % item for item in X_train])
        f4.writelines(["%s\n" % item for item in y_train])
        f5.writelines(["%s\n" % item for item in X_test])
        f6.writelines(["%s\n" % item for item in y_test])

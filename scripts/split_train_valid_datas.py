import numpy as np
from sklearn.cross_validation import train_test_split

if __name__ == '__main__':
    X = np.loadtxt('../data/dev.en', dtype=str)
    y = np.loadtxt('../data/dev.zh', dtype=str)
    # X = np.loadtxt('../stf_data/train.en')
    # y = np.loadtxt('../stf_data/train_ctb_seg.zh')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)
    np.savetxt('../data/train_split.en', X_train)
    np.savetxt('../data/train_split.zh', y_train)
    np.savetxt('../data/test_split.en', X_test)
    np.savetxt('../_data/test_split.zh', y_test)
    # np.savetxt('../stf_data/train_split.en', X_train)
    # np.savetxt('../stf_data/train_split.zh', y_train)
    # np.savetxt('../stf_data/test_split.en', X_test)
    # np.savetxt('../stf_data/test_split.zh', y_test)

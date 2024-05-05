import React from 'react';
import {StyleSheet, Text, View} from 'react-native';

import {getFileType} from '../utils';

export const FileDisplay = ({file}: {file: string}) => {
  return (
    <>
      <View style={styles.file}>
        <Text style={styles.filename}>{file}</Text>
        <Text style={styles.filetype}>{getFileType(file)}</Text>
      </View>
    </>
  );
};
const styles = StyleSheet.create({
  filename: {
    fontWeight: '700',
    paddingRight: 20,
  },
  filetype: {
    fontStyle: 'italic',
    fontWeight: '400',
  },
  file: {
    flexDirection: 'row',
    height: 40,
    padding: 10,
  },
});

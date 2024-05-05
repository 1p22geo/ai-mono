import React, {useCallback, useEffect, useState} from 'react';
import {Button, StyleSheet, Text} from 'react-native';

import DocumentPicker from 'react-native-document-picker';
import {fetchFileList, sendFile} from './utils';
import {FileDisplay} from './FileDisplay';

export const RagStore = () => {
  const [files, setFiles] = useState<string[]>([]);
  useEffect(() => {
    fetchFileList().then(res => {
      setFiles(res);
    });
  }, []);

  const handleDocumentSelection = useCallback(async () => {
    try {
      const response = await DocumentPicker.pick({
        allowMultiSelection: false,
        presentationStyle: 'fullScreen',
      });
      await sendFile(response);
      setFiles(await fetchFileList());
    } catch (err: any) {
      console.warn(err);
    }
  }, []);
  return (
    <>
      <Text style={styles.title}>RAG store</Text>
      <Button title="UPLOAD FILE" onPress={handleDocumentSelection} />
      {files.map(file => (
        <FileDisplay file={file} key={file} />
      ))}
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
  title: {
    fontSize: 32,
  },
  highlight: {
    fontWeight: '700',
  },
});

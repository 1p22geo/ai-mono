import { constants } from '../constants';
import { DocumentPickerResponse } from 'react-native-document-picker';

export const fetchFileList = async () => {
  const res = await fetch(new URL('/files', constants.ENDPOINT_URI), {
    headers: {
      'ngrok-skip-browser-warning': 'true'
    }
  });
  const json = await res.json();
  return json;
};

export const sendFile = async (response: DocumentPickerResponse[]) => {
  if (response.length !== 1) {
    throw 'sendFile can only be used with single files';
  }
  let data = new FormData();
  data.append('file', {
    uri: response[0].uri,
    type: response[0].type,
    name: response[0].name,
  });
  await fetch(new URL('/upload', constants.ENDPOINT_URI), {
    method: 'POST',
    headers: {
      'Content-Type': 'multipart/form-data',
      'ngrok-skip-browser-warning': 'true'
    },
    body: data,
  });
};

export const getFileType = (filename: string) => {
  switch (filename.split('.').at(-1)) {
    case 'txt':
      return 'Text file';
    case 'wav':
      return 'WAV Sound recording';
    case 'pdf':
      return 'PDF document';
    default:
      return '<<unknown>>';
  }
};

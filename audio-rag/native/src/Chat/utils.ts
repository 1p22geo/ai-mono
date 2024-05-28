import { Dispatch, SetStateAction } from 'react';
import { Message } from './types';
import { constants } from '../constants';

export interface ResponseMessage {
  answer: string;
  context: {
    metadata: {
      source: string;
    };
    page_content: string;
    type: string;
  }[];
}

export const sendMessage = async (
  message: string,
): Promise<ResponseMessage> => {
  const res = await fetch(new URL('/api/query', constants.ENDPOINT_URI), {
    headers: {
      'Content-Type': 'application/json',
      'ngrok-skip-browser-warning': 'true'
    },
    body: JSON.stringify({
      prompt: message,
    }),
    method: 'POST',
  });
  return await res.json();
};

export const queueMessage = (
  message: string,
  setMessages: Dispatch<SetStateAction<Message[]>>,
) => {
  sendMessage(message).then((res: ResponseMessage) => {
    setMessages(messages =>
      messages.concat([
        {
          author: 'RAG',
          content: res.answer,
          context: res.context.map(item => ({
            source: item.metadata.source,
            content: item.page_content,
          })),
        },
      ]),
    );
  });
};

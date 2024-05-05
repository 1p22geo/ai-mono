export interface Message {
  author: 'RAG' | 'User';
  content: string;
  context?: MessageContext[];
}

export interface MessageContext {
  source: string;
  content: string;
}

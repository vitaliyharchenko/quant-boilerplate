// @flow

import React from 'react';

import type { Text } from '../types/blocks';

export type Props = {
  onClick: () => void,
  completed: boolean,
  text: Text
};

const Block = ({ onClick, completed, text }: Props) => (
  <li
    onClick={onClick}
    style={{
      textDecoration: completed ? 'line-through' : 'none'
    }}
  >
    {text}
  </li>
);

export default Block;
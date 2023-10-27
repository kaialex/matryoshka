import numpy as np
import pandas as pd
import streamlit as st

def checkAnswer(input_array: np.ndarray):
  #係数行列 array_d
  array = np.array([[1-input_array[0,0], -input_array[0,1], -input_array[0,2]],[-input_array[1,0], 1-input_array[1,1], -input_array[1,2]],[-input_array[2,0], -input_array[2,1], 1-input_array[2,2]]])
  #拡散係数行列
  array_d = np.array([[input_array[0,3]],[input_array[1,3]],[input_array[2,3]]])
  
  #2つの係数をconcatenate
  array_coef = np.concatenate([array,array_d],1)

  rank_array = np.linalg.matrix_rank(array)
  rank_array_coef = np.linalg.matrix_rank(array_coef)

  #解がある場合の条件は、係数行列のランクと拡散係数行列のランクが等しいこと
  #解がただ一つの条件は、係数行列のランクと拡散係数行列のランクが等しく、係数行列のランクが変数の数と等しいこと

  if rank_array == rank_array_coef and rank_array == 3:
    st.write("解はただ一つです")
    st.write("解は")
    st.write(np.linalg.solve(array,array_d))
  elif rank_array == rank_array_coef and rank_array <= 3:
    st.write("解は無数にあります")
  else:
    st.write("解はありません")

def calculate(df: pd.DataFrame):
  input_array = df.to_numpy()
  checkAnswer(input_array)

def main():
  data_df = pd.DataFrame(
    {
        "A": [0, 0, 0],
        "B": [0, 0, 0],
        "C": [0, 0, 0],
        "定数値": [0, 0, 0],
    },
    index=["A=", "B=", "C="],
  )

  edited_df = st.data_editor(
      data_df,
  )
  
  btn = st.button("計算")
  
  if btn:
    calculate(edited_df)

if __name__ == "__main__":
  main()
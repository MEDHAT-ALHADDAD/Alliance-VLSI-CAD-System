
--
-- Generated by VASY
--
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY fulladder_x4 IS
PORT(
  a1	: IN STD_LOGIC;
  a2	: IN STD_LOGIC;
  a3	: IN STD_LOGIC;
  a4	: IN STD_LOGIC;
  b1	: IN STD_LOGIC;
  b2	: IN STD_LOGIC;
  b3	: IN STD_LOGIC;
  b4	: IN STD_LOGIC;
  cin1	: IN STD_LOGIC;
  cin2	: IN STD_LOGIC;
  cin3	: IN STD_LOGIC;
  cout	: OUT STD_LOGIC;
  sout	: OUT STD_LOGIC
);
END fulladder_x4;

ARCHITECTURE RTL OF fulladder_x4 IS
  SIGNAL ncout	: STD_LOGIC;

BEGIN
  cout <= NOT(ncout);
  sout <= (((a3 AND b3) AND cin2) OR (((a4 OR b4) OR cin3) AND ncout));
  ncout <= NOT(((a1 AND b1) OR ((a2 OR b2) AND cin1)));
END RTL;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;
use ieee.std_logic_textio.all;

entity g07_lab2_tb_Batch2 is
end g07_lab2_tb_Batch2;

architecture test of g07_lab2_tb_Batch2 is

component g07_lab2_Batch2 is
	port(x    : in std_logic_vector(7 downto 0);
	     y    : in std_logic_vector(7 downto 0);
	     N    : in std_logic_vector(7 downto 0);
	     clk  : in std_logic;
	     rst  : in std_logic;
	     mac  : out std_logic_vector(17 downto 0);
	     ready: out std_logic);
end component g07_lab2_Batch2;

file file_VECTORS_X: text;
file file_VECTORS_Y: text;
file file_RESULTS: text;

constant clk_PERIOD : time := 100 ns;

signal x_in     : std_logic_vector(7 downto 0);
signal y_in     : std_logic_vector(7 downto 0);
signal N_in     : std_logic_vector(7 downto 0);
signal clk      : std_logic;
signal rst      : std_logic;
signal mac_out  : std_logic_vector(17 downto 0);
signal ready_out: std_logic;

begin
	g07_MAC_INST: g07_lab2_Batch2
	port map(
	 x => x_in,
	 y => y_in,
	 N => N_in,
	 clk => clk,
	 rst => rst,
	 mac => mac_out,
	 ready => ready_out);

clk_generation : process
  begin 
    clk <= '1';
    wait for clk_PERIOD/2;
    clk <= '0';
    wait for clk_PERIOD/2;
  end process clk_generation;	


feeding_inst : process is
  variable v_Iline1 : line;
  variable v_Iline2 : line;
  variable v_Oline : line;
  variable v_x_in : std_logic_vector(7 downto 0);
  variable v_y_in : std_logic_vector(7 downto 0);
  begin
  
    N_in <= "11001000";
    rst <= '1';
    wait until rising_edge(clk);
    wait until rising_edge(clk);
    rst <= '0';

    file_open(file_VECTORS_X,"lab2-x-fixed-point-batch2.txt",read_mode);
    file_open(file_VECTORS_Y,"lab2-y-fixed-point-batch2.txt",read_mode);
    file_open(file_RESULTS,"lab2-out-batch2.txt",write_mode);
    ready_out <= '1';

    while not endfile (file_VECTORS_X) loop
      readline(file_VECTORS_X, v_Iline1);
      read(v_Iline1, v_x_in);
      readline(file_VECTORS_Y, v_Iline2);
      read(v_Iline2, v_y_in);
  
      x_in <= v_x_in;
      y_in <= v_y_in;

     
        write(v_Oline, mac_out);
        writeline(file_RESULTS, v_Oline);
      
    
      wait until rising_edge(clk);
    end loop;
  
    wait;
  
  end process feeding_inst;

end architecture test;


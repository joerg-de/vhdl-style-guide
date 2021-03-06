Instantiation Rules
-------------------

instantiation_001
#################

This rule checks for the proper indentation of instantiations.

**Violation**

.. code-block:: vhdl

     U_FIFO : FIFO
  port map (
           WR_EN    => wr_en,
   RD_EN    => rd_en,
         OVERFLOW => overflow
                );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

instantiation_002
#################

This rule checks for a single space after the :.

**Violation**

.. code-block:: vhdl

   U_FIFO :FIFO

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO

instantiation_003
#################

This rule checks for a single space before the :.

**Violation**

.. code-block:: vhdl

   U_FIFO: FIFO

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO

instantiation_004
#################

This rule checks for a blank line above the instantiation.

.. NOTE:: Comments are allowed above the instantiation.

**Violation**

.. code-block:: vhdl

   WR_EN <= '1';
   U_FIFO : FIFO

   -- Instantiate another FIFO
   U_FIFO2 : FIFO

**Fix**

.. code-block:: vhdl

   WR_EN <= '1';

   U_FIFO : FIFO

   -- Instantiate another FIFO
   U_FIFO2 : FIFO

instantiation_005
#################

This rule checks the instantiation declaration and the **port map** keywords are not on the same line.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO port map (

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (

instantiation_006
#################

This rule checks the **port map** keywords have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PORT MAP (

**Fix**

.. code-block:: vhdl

   port map (

instantiation_007
#################

This rule checks the closing ) for the port map is on it's own line.

**Violation**

.. code-block:: vhdl

    WR_EN => wr_en);

**Fix**

.. code-block:: vhdl

      WR_EN => wr_en
    );

instantiation_008
#################

This rule checks the instance name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   U_FIFO : fifo

**Fix**

.. code-block:: vhdl

   u_fifo : fifo

instantiation_009
#################

This rule checks the entity name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   u_fifo : FIFO


**Fix**

.. code-block:: vhdl

   u_fifo : fifo

instantiation_010
#################

This rule checks the alignment of the **=>** operator for each generic and port in the instantiation.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.
**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       g_width => 8
       g_delay    => 2
     )
     port map (
       wr_en => wr_en,
       rd_en => rd_en,
       overflow => overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       g_width => 8
       g_delay => 2
     )
     port map (
       wr_en    => wr_en,
       rd_en    => rd_en,
       overflow => overflow
     );

instantiation_011
#################

This rule checks the port name is uppercase.
Indexes on ports will not be uppercased.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       wr_en              => wr_en,
       rd_en              => rd_en,
       OVERFLOW           => overflow,
       underflow(c_index) => underflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN              => wr_en,
       RD_EN              => rd_en,
       OVERFLOW           => overflow,
       UNDERFLOW(c_index) => underflow
     );

instantiation_012
#################

This rule checks the instantiation declaration and the **generic map** keywords are not on the same line.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO generic map (

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (

instantiation_013
#################

This rule checks the **generic map** keywords have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   GENERIC MAP (

**Fix**

.. code-block:: vhdl

   generic map (

instantiation_014
#################

This rule checks for the closing parenthesis *)* on generic maps are on their own line.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME
     generic map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE)

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME
     generic map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE
     )

instantiation_016
#################

This rule checks generic names have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   u_fifo : fifo
     generic map (
       DEPTH => 512,
       WIDTH => 32
     )

**Fix**

.. code-block:: vhdl

   u_fifo : fifo
     generic map (
       depth => 512,
       width => 32
     )


instantiation_017
#################

This rule checks if the **generic map** keywords and a generic assignment are on the same line.

**Violation**

.. code-block:: vhdl

     generic map (DEPTH => 512,
       WIDTH => 32
     )

**Fix**

.. code-block:: vhdl

     generic map (
       DEPTH => 512,
       WIDTH => 32
     )

instantiation_018
#################

This rule checks for a single space between the **map** keyword and the (.

**Violation**

.. code-block:: vhdl

   generic map(

   generic map   (

**Fix**

.. code-block:: vhdl

   generic map (

   generic map (

instantiation_019
#################

This rule checks for a blank line below the end of the instantiation declaration.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );
   U_RAM : RAM

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

   U_RAM : RAM

instantiation_020
#################

This rule checks for a port assignment on the same line as the **port map** keyword.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

instantiation_021
#################

This rule checks multiple port assignments on the same line.

**Violation**

.. code-block:: vhdl

   port map (
     WR_EN => w_wr_en, RD_EN => w_rd_en,
     OVERFLOW => w_overflow
   );

**Fix**

.. code-block:: vhdl

   port map (
     WR_EN => w_wr_en,
     RD_EN => w_rd_en,
     OVERFLOW => w_overflow
   );

instantiation_022
#################

This rule checks for a single space after the **=>** operator in port maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    =>   wr_en,
       RD_EN    =>rd_en,
       OVERFLOW =>     overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

instantiation_023
#################

This rule checks for comments at the end of the port and generic assignments in instantiations.
These comments represent additional maintainence.
They will be out of sync with the entity at some point.
Refer to the entity for port types, port directions and purpose.

**Violation**

.. code-block:: vhdl

   WR_EN => w_wr_en;   -- out : std_logic
   RD_EN => w_rd_en;   -- Reads data when asserted

**Fix**

.. code-block:: vhdl

   WR_EN => w_wr_en;
   RD_EN => w_rd_en;

instantiation_024
#################

This rule checks for positional generics and ports.
Positional ports and generics are subject to problems when the position of the underlying component changes.

**Violation**

.. code-block:: vhdl

   port map (
     WR_EN, RD_EN, OVERFLOW
   );

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   port map (
     WR_EN    => WR_EN;
     RD_EN    => RD_EN;
     OVERFLOW => OVERFLOW
   );

instantiation_025
#################

This rule checks the ( is on the same line as the **port map** keywords.

**Violation**

.. code-block:: vhdl

   port map
   (
     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   port map (
     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

instantiation_026
#################

This rule checks the ( is on the same line as the **generic map** keywords.

**Violation**

.. code-block:: vhdl

   generic map
   (
     WIDTH => 32,
     DEPTH => 512
   )

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   generic map (
     WIDTH => 32,
     DEPTH => 512
   )

instantiation_027
#################

This rule checks the **entity** keyword has proper case in direct instantiations.
 
Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY library.ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : entity library.ENTITY_NAME

instantiation_028
#################

This rule checks the entity name has proper case in direct instantiations.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   instance_name : entity library.ENTITY_NAME

**Fix**

.. code-block:: vhdl

   instance_name : entity library.entity_name

instantiation_029
#################

This rule checks for alignment of inline comments in an instantiation.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.
**Violation**

**Violation**

.. code-block:: vhdl

       wr_en    => write_enable,        -- Wrte enable
       rd_en    => read_enable,    -- Read enable
       overflow => overflow,         -- FIFO has overflowed

**Fix**

.. code-block:: vhdl

       wr_en    => write_enable, -- Wrte enable
       rd_en    => read_enable,  -- Read enable
       overflow => overflow,     -- FIFO has overflowed

instantiation_030
#################

This rule checks for a single space after the **=>** keyword in generic maps.

**Violation**

.. code-block:: vhdl

   generic map
   (
     WIDTH =>    32,
     DEPTH => 512
   )

**Fix**

.. code-block:: vhdl

   generic map
   (
     WIDTH => 32,
     DEPTH => 512
   )

instantiation_031
#################

This rule checks the component keyword has proper case in component instantiations that use the **component** keyword.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   instance_name : COMPONENT entity_name

**Fix**

.. code-block:: vhdl

   instance_name : component entity_name

.. NOTE:: This rule is off by default.
   If this rule is desired, then enable this rule and disable instantiation_033. 

   .. code-block:: json
   
      {
        "rule":{
          "instantiation_031":{
             "disable":"False"
          },
          "instantiation_033":{
             "disable":"True"
          }
        }
      }

instantiation_032
#################

This rule checks for a single space after the **component** keyword if it is used.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME
   INSTANCE_NAME : component   ENTITY_NAME
   INSTANCE_NAME : component  ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME
   INSTANCE_NAME : component ENTITY_NAME
   INSTANCE_NAME : component ENTITY_NAME

.. NOTE:: This rule is off by default.
   If this rule is desired, then enable this rule and disable instantiation_033. 

   .. code-block:: json
   
      {
        "rule":{
          "instantiation_032":{
             "disable":"False"
          },
          "instantiation_033":{
             "disable":"True"
          }
        }
      }

instantiation_033
#################

This rule checks for the **component** keyword and will remove it.

The component keyword is optional and does not provide clarity.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME

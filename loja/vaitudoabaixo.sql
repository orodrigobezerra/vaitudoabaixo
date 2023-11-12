-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Tempo de geração: 03-Nov-2023 às 13:39
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `vaitudoabaixo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `article`
--

CREATE TABLE `article` (
  `ARTICLE_ID` int(20) NOT NULL,
  `NAME` char(100) NOT NULL,
  `COLOR` char(50) NOT NULL,
  `INSTRUMENT` char(200) NOT NULL,
  `QTY_STOCK` int(10) NOT NULL,
  `PRICE` decimal(20,0) NOT NULL,
  `IMAGE` char(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `article`
--

INSERT INTO `article` (`ARTICLE_ID`, `NAME`, `COLOR`, `INSTRUMENT`, `QTY_STOCK`, `PRICE`, `IMAGE`) VALUES
(2, 'Fender Gold Foil Ebony Fingerboard', 'Candy Apple Burst', 'Eletrica', 40, 945, 'https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/_55/558842/17889262_800.jpg'),
(3, 'Ibanez AZS2200-BK Prestige B-Stock', 'Black', 'Eletrica', 33, 1392, 'https://images.musicstore.de/images/1280/ibanez-azs2200-bk-prestige-black-_1_GIT0055975-000.jpg'),
(4, 'Charvel Pro-Mod So-Cal Style 2 24 HH HT CM Caramelized Maple Fingerboard Robins', 'Egg Blue', 'Eletrica', 25, 682, 'https://www.fmicassets.com/Damroot/CharvelPDP/10001/2966561527_cha_ins_frt_01_rr.jpg'),
(5, 'Fender American Vintage II 1963 Rosewood Fingerboard', 'Surf Green', 'Eletrica', 8, 1572, 'https://images.guitarguitar.co.uk/cdn/large/170/220707388645008f.jpg'),
(6, 'Fender SQ 40th Anni. Vintage Edition Maple Fingerboard Black Anodized Pickguard Satin', 'Vintage Blonde', 'Eletrica', 50, 377, 'https://media.guitarcenter.com/is/image/MMGS7/L92323000003000-00-600x600.jpg'),
(7, 'Ibanez RG5320C Prestige', 'Pearl White', 'Eletrica', 10, 1531, 'https://gjmsoundpr.com/cdn/shop/products/squier-40th-anniversary-stratocaster-vintage-edition-maple-fingerboard-black-anodized-pickguard-satin-wide-2-color-sunburst-429758.jpg?v=1681768970'),
(8, 'Fender Made in Japan Hybrid II HSS Limited Run Reverse Telecaster Head Maple Ocean', 'Turquoise Metallic', 'Eletrica', 30, 1029, 'https://andertons-productimages.imgix.net/5502502308-Fender-MIJ-Hybrid-II-Stratocaster-HSS-Reverse-Telecaster-Headstock-Ocean-Turquoise-Metallic.png'),
(9, 'Gretsch G2217 Streamliner Junior Jet', 'Fiesta Red', 'Eletrica', 30, 251, 'https://produtos.egitana.pt/gretsch-g2217-streamliner-junior-jet-fiesta-red_606f1c6b52cbb.jpg?v=2022-03-21%2017:53:59'),
(10, 'Edwards JAPAN LPS', 'Cherry Sunburst', 'Eletrica', 50, 765, 'https://www.promusictools.com/media/catalog/product/cache/1/image/1200x800/bd5be3e4bffe87df985139cc5e5c836c/e/s/esp-edwards-e-lp-98lts_chs.jpg'),
(11, 'FGretsch G5420T Electromatic Classic Bigsby Laurel Fingerboard', 'Orange Stain', 'Eletrica', 20, 613, 'https://m.media-amazon.com/images/I/31HN7hhHhnL.jpg'),
(38, 'Fender SQ 40th Anni. Jazz Bass Vintage Edition Maple Fingerboard Black Anodized Pickguard Satin Wide', 'Sunburst', 'Baixo', 20, 336, 'https://billyhydemusic.com.au/media/catalog/product/cache/d91c07a171ff745181b6b8079564e586/0/3/0379541502_sqr_ins_frt_1_rr.jpg'),
(39, 'Ibanez TMB30', 'Mint Green', 'Baixo', 10, 180, 'https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/_38/387082/13107836_800.jpg'),
(40, 'Yamaha BB734 A TMBL', 'Black', 'Baixo', 50, 803, 'https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/_50/503165/16849861_800.jpg'),
(41, 'Jackson JS Series Spectra Bass JS3V Laurel Fingerboard', 'Indigo Blue', 'Baixo', 15, 352, 'https://images.reverb.com/image/upload/s--JQlg0c13--/f_auto,t_large/v1677264271/yq5im5oligzowtbnqmrw.jpg'),
(42, 'Yamaha BB235 RBR', 'Raspberry Red', 'Baixo', 12, 370, 'https://produtos.egitana.pt/yamaha-bb235-rbr-raspberry-red_63ecca771d164.jpg'),
(43, 'Fender Monterey Standard', 'Natural', 'Acustica', 20, 202, 'https://bimotordj.com/image/cache/catalog/097-3052-122/Fender%20Monterey%20Standard%20MAH%20WB%20Bimotordj%201-1200x900.jpg'),
(44, 'Yamaha FG 800 M', 'Natural', 'Acustica', 20, 228, 'https://www.lojamusica.com/5220-large_default/guit-folk-yamaha-fg-800m.jpg'),
(45, 'Gretsch G9520E Gin Rickey', 'Black', 'Acustica', 5, 229, 'https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/_49/497845/16226146_800.jpg'),
(46, 'Fender Sonoran Mini', 'Mahogany', 'Acustica', 20, 128, 'https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/_49/497167/16349083_800.jpg'),
(47, 'Gretsch G5022CWFE Falcon Rancher B-Stock', 'White', 'Acustica', 15, 455, 'https://m.media-amazon.com/images/I/31-DVAA+FfL.jpg');

-- --------------------------------------------------------

--
-- Estrutura da tabela `invoice`
--

CREATE TABLE `invoice` (
  `INVOICE_ID` int(20) NOT NULL,
  `CART_ID` int(20) NOT NULL,
  `PRICE` decimal(20,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `shoppingcart`
--

CREATE TABLE `shoppingcart` (
  `CART_ID` int(20) NOT NULL,
  `CART_LINES_ID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `shoppingcartlines`
--

CREATE TABLE `shoppingcartlines` (
  `CART_LINES_ID` int(20) NOT NULL,
  `ARTICLE_ID` int(20) NOT NULL,
  `QTY` int(20) NOT NULL,
  `USER_ID` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `users`
--

CREATE TABLE `users` (
  `USER_ID` int(20) NOT NULL,
  `USER_NAME` char(50) NOT NULL,
  `EMAIL` char(50) NOT NULL,
  `PASSWORD` char(15) NOT NULL,
  `APAGADO` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `users`
--

INSERT INTO `users` (`USER_ID`, `USER_NAME`, `EMAIL`, `PASSWORD`, `APAGADO`) VALUES
(2, 'Rodrigo', 'rodrigo@123.com', '1234', 1),
(3, 'Rodrigo B', 'rodrigo_b@123.com', '1234', 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `wishlist`
--

CREATE TABLE `wishlist` (
  `WISH_ID` int(20) NOT NULL,
  `WISH_LINES_ID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `wishlistlines`
--

CREATE TABLE `wishlistlines` (
  `WISH_LINES_ID` int(20) NOT NULL,
  `ARTICLE_ID` int(20) NOT NULL,
  `QTY` int(20) NOT NULL,
  `USER_ID` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`ARTICLE_ID`);

--
-- Índices para tabela `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`INVOICE_ID`);

--
-- Índices para tabela `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD PRIMARY KEY (`CART_ID`);

--
-- Índices para tabela `shoppingcartlines`
--
ALTER TABLE `shoppingcartlines`
  ADD PRIMARY KEY (`CART_LINES_ID`);

--
-- Índices para tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`USER_ID`);

--
-- Índices para tabela `wishlist`
--
ALTER TABLE `wishlist`
  ADD PRIMARY KEY (`WISH_ID`);

--
-- Índices para tabela `wishlistlines`
--
ALTER TABLE `wishlistlines`
  ADD PRIMARY KEY (`WISH_LINES_ID`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `article`
--
ALTER TABLE `article`
  MODIFY `ARTICLE_ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de tabela `invoice`
--
ALTER TABLE `invoice`
  MODIFY `INVOICE_ID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `shoppingcart`
--
ALTER TABLE `shoppingcart`
  MODIFY `CART_ID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `shoppingcartlines`
--
ALTER TABLE `shoppingcartlines`
  MODIFY `CART_LINES_ID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `USER_ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `wishlist`
--
ALTER TABLE `wishlist`
  MODIFY `WISH_ID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `wishlistlines`
--
ALTER TABLE `wishlistlines`
  MODIFY `WISH_LINES_ID` int(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

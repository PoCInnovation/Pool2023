# Day 5 - IPFS : INTER PLANETARY FILE SYSTEM

✔️ Create Node

✔️ Mesh Network

✔️ Bitswap

✔️ Distributed Hash Table (DHT)

## Notions
* Node
* Filesystem
* Mesh Network
* Bitswap
* Distributed Hash Table (DHT)

## Introduction

Pour cet matine nous allons utiliser une implementation d'IPFS en Go.
Cette implementation est la plus utilise aujourd'hui et la plus complete.
Il existe egalement de mutilples implementation Iroh en Rust, Js et bien d'autres.

Il n'est pas necessaire d'avoir fait du Go, l'objectif est de comprendre la technologie et pour ce nous utiliserons la CLI.

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file.

## Step 1 - Create CID

### :bookmark_tabs: **Description**:

### :pushpin: **Tasks**:

- Nous allons creer un fichier appele `Hello_World.txt` dans celui ci, nous allons ecrire `Hello World !`.
  L'objectif est de creer un CID a partir de ce fichier.
- Trouvez la commande permettant de creer un CID a partir d'un contenu de type fichier.


### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

!Script de correction

Et voila, nous avons creer notre premier CID !
Il est maintenant accessible sur notre machine et vous pouvez le retrouver dans `$HOME/.ipfs/blocks`

Une des particularite de votre CID est qu'il commence toujours par Qm. C'est ce qu'on appel un CID de version 1.

Notre objectif est maintenant de creer un CID v0 avec le meme contenu.
Nous avons maintenant un nouveau CID avec le meme contenu ?

La question est : Qu'avons nous dans notre `$HOME/.ipfs/blocks` ? Deux fichiers identiques ?

## Step 2 - Custom CID

### :bookmark_tabs: **Description**:

Il est bien d'utiliser du SHA-2 mais le SHA-1 c'est mieux !
On va aller un peu plus loin. Dans le fichier `./utils`, on peut retrouver deux image nommme IAmA.jpg and IAmB.jpg.
Par groupe de deux, vous allez chacun choisir une image differente et creer un CID avec pour hash le SHA-1.

Quel est concretement la difference entre le SHA-1 et SHA-2 ?

Le Hash d'un contenu est une fonction mathematique permettant d'avoir toujours le meme output avec un input donnee.
L'inverse n'est malheureusement pas possible. Cette pratique est utilise pour stocker les mots de passe par exemple.
On va verifier l'egalite entre notre mot de passe que l'on va hasher et le mot de passe deja hasher en base de donnee.
Si celui ci est identique, c'est que  le mot de passe donne en input est correct.
De plus, si notre base de donnee leak, le malandrin aura seulement des hashes qu'il ne pourra pas reverse.

Mais on peut se poser la question : Quel est l'utilite de plusieurs algorithm de Hashage.
Il est possible d'obtenir deux hash identique avec des contenu different, ce qu'on appel une collision de Hash.
Si nous reprenons notre exemple de base de donnee, il serait dont possible d'obtenir le meme hash sans avoir un mot de passe identique.
Vous l'aurez devine, avec le SHA-1 nous somme capable de faire des collisions de Hash.

### :pushpin: **Tasks**:

- Il est maintenant temps de hash notre photo et de voir ce que l'on va obtenir.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

!Script Correction

Felicitation ! Nous avons obtenu le meme hash avec deux contenu visiblement different.

Il vous est possible de changer la taille de votre bloc et d'autres choses encore plus passionnante mais nous allons passer tres vite a la suite !


## Step 3 - My name is Daemon

### :bookmark_tabs: **Description**:

Vous l'aurez remarquer, il est possible de creer des CID mais personne peut actuellement communiquer avec vous.
Personne ? Plus pour longtemps. Il est temps de s'ouvrir au monde du p2p.

### :pushpin: **Tasks**:

- Lancer votre daemon ipfs.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

YES ! Let's do it !
Vous pouvez maintenant echanger et recuperer du contenu partout dans le monde. Comment faire ?

## Step 4 - Get my content

### :bookmark_tabs: **Description**:

Voici le CID qui va vous etre utilse : CID....
Nous avons vu qu'on CID point vers un contenu. En effecuter une commande GET nous devrions etre capable de retrouver le contenu desire.

### :pushpin: **Tasks**:

- Recuperer ce contenu, il est possible que ce contenu mette du temps a etre recuperer. Votre daemon va demander a toutes les personnes que vous connaissez sur le reseau.


### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

Ouvrez le contenu une fois recu !
Si votre contenu est identique a !image vous avez reussi !

Ca va bien plus vite que prevu !

## Step 5 - One, Two, Three ... Replication

### :bookmark_tabs: **Description**:

Il est utile de recuperer du contenu, mais le mieux est de le replication aussi connu sous le nom de pinner.
Cela va permettre d'ecrire de la metadata est d'exprimer que vous ne souhaitez pas supprimer le contenu.

REPLICATIONNNNN ! Nous sommes maintenant plusieurs a avoir notre contenu.
Plus vous avez de noeuds avec votre contenu pinner, plus vous allez avoir la recuperer et l'echange de contenu sera rapide.

Il existe des services de pinning qui vous permet d'utiliser des machines afin de pinner des contenu.

EXAMPLE : Pinata, Scaleway. Vous avez meme des blockchains dediee a recompenser par des Tokens les gens qui mettents a
disposition leurs machines (Filecoin).

### :pushpin: **Tasks**:

- A l'aide du CID, faites un pin du contenu.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

Verifier a l'aide de la commande `ipfs pin ls` que votre contenu est bien pin.

## Step 6 - One, Two, Three ... Replication

### :bookmark_tabs: **Description**:

Maintenant que notre contenu est pinner. Nous allons supprimer tous les blocks inutiles,
Il existe plusieurs type de garbage collector en informatique.
Le garbage collector en programmation qui vous permet de free votre memoire de maniere automatique commme le python ou le JS.
Et celui qui permet de supprimer des blocks sur les filesystems.

### :pushpin: **Tasks**:

- Devinez lequel nous allons utiliser :eyes:

Cette commande est un peu plus complique a trouver mais vous allez y arriver !
Le `gc`, n'est par defaut pas activer sur vos noeuds.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

!Script Correction

## Step 7 - Garbage Collector

### :bookmark_tabs: **Description**:

Maintenant que notre contenu est pinner. Nous allons supprimer tous les blocks inutiles,
Il existe plusieurs type de garbage collector en informatique.
Le garbage collector en programmation qui vous permet de free votre memoire de maniere automatique commme le python ou le JS.
Et celui qui permet de supprimer des blocks sur les filesystems.

### :pushpin: **Tasks**:

- Devinez lequel nous allons utiliser :eyes:

Cette commande est un peu plus complique a trouver mais vous allez y arriver !
Le `gc`, n'est par defaut pas activer sur vos noeuds.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

!Script Correction

## Step 8 - Turn Off

### :bookmark_tabs: **Description**:

Nous allons nous assurer de toujours avoir notre contenu, Mais avant ca pour ne pas etre biaiser, nous allons eteindre notre daemon.
Sinon, il est possible sans le savoir de recuperer le contenu d'un autre noeud.

### :pushpin: **Tasks**:

- Deconnecter votre neoud du reseau.
- Pour ca besoin de couper votre connexion internet :sink:

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

!Script Correction

## Step 9 - Unpin content

### :bookmark_tabs: **Description**:

Rappelons nous, tout a l'heure nous avons pin un contenu. C'est a dire qu'il est permanent sur notre machine.
Il serait bien d'update notre metadata pour qu'au prochain gc, il puisse etre supprime.

### :pushpin: **Tasks**:

- L'objectif est d'unpin notre CID.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

Verifier bien a l'aide `ipfs pin ls` que votre cid n'est pas existant

## Step 10 - Back to the past

### :bookmark_tabs: **Description**:

Si toutes les etapes ce sont bien passe, nous ne devrions etre capable de faire passer le GC et voir nos blocs disparaitre a tout jamais.

### :pushpin: **Tasks**:

- Refaite passer le GC

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

Votre CID doit etre afficher sur votre shell apres la commande.

## Step 11 - Node automatic

### :bookmark_tabs: **Description**:

Nous avons pu observer pas mal de souci sur notre neoud.

Pourquoi notre GC ne passe pas par defaut ?

### :pushpin: **Tasks**:

Nous allons parametrer notre noeud pour que notre GC passe toutes les 10 min.
N'oubliez pas de faire la commande `ipfs init` pour prendre en compte vos changement.

### :books: **Documentation**:

- [[NOTION]](http://link.com)
- [[NOTION]](http://link.com)

### ✔️ **Validation**:

!Script Correction

## Bonus - [NAME]

[BONUS TASKS, TO GO FURTHER]

## Conclusion

Well done ! You've accomplished a lot with IPFS, and there is so much more to discover.
Refer to the [official documentation](https://link.com) to deep-dive into it.

Hope you enjoyed the workshop !

## Authors

| [<img src="https://github.com/Doozers.png?size=85" width=85><br><sub>Isma</sub>](https://github.com/Doozers) | 
|:------------------------------------------------------------------------------------------------------------:|
<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white">
    </a>
</p>

> :rocket: Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.

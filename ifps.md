# IPFS : INTER PLANETARY FILE SYSTEM

## What is filesystem ?

## Notions
* Node
* Filesystem
* Mesh Network
* Bitswap
* Distributed Hash Table (DHT)

## Installation Kubo

Pour cet matine nous allons utiliser une implementation d'IPFS en Go.
Cette implementation est la plus utilise aujourd'hui et la plus complete.
Il existe egalement de mutilples implementation Iroh en Rust, Js et bien d'autres.

Il n'est pas necessaire d'avoir fait du Go, l'objectif est de comprendre la technologie et pour ce nous utiliserons la CLI.

```shell
# Arch Linux
sudo pacman -S kubo

# Ubuntu
apt install kubo

# Fedora

dnf install kubo
```

## Exercises CLI

### I. Introduction

#### !.0 - Create CID

Nous allons creer un fichier appele `Hello_World.txt` dans celui ci, nous allons ecrire `Hello World !`.
L'objectif est de creer un CID a partir de ce fichier.

!Script de correction

Et voila, nous avons creer notre premier CID !
Il est maintenant accessible sur notre machine et vous pouvez le retrouver dans `$HOME/.ipfs/blocks`

Une des particularite de votre CID est qu'il commence toujours par Qm. C'est ce qu'on appel un CID de version 1.

Notre objectif est maintenant de creer un CID v0 avec le meme contenu.
Nous avons maintenant un nouveau CID avec le meme contenu ?

La question est : Qu'avons nous dans notre `$HOME/.ipfs/blocks` ? Deux fichiers identiques ?

#### 2.0 Custom CID

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

Il est maintenant temps de hash notre photo et de voir ce que l'on va obtenir.

Felicitation ! Nous avons obtenu le meme hash avec deux contenu visiblement different.

Il vous est possible de changer la taille de votre bloc et d'autres choses encore plus passionnante mais nous allons passer tres vite a la suite !

### II. Hello World

#### 1.0 My name is Daemon

Vous l'aurez remarquer, il est possible de creer des CID mais personne peut actuellement communiquer avec vous.
Personne ? Plus pour longtemps. Il est temps de s'ouvrir au monde du p2p.
Lancer votre daemon ipfs.

YES ! Let's do it !
Vous pouvez maintenant echanger et recuperer du contenu partout dans le monde. Comment faire ?

#### 2,0 Get my content

Voici le CID qui va vous etre utiles : CID....

Recuperer ce contenu, il est possible que ce contenu mette du temps a etre recuperer. Votre daemon va demander a toutes les personnes que vous connaissez sur le reseau.

Ouvrez le contenu une fois recu !

Ca va bien plus vite que prevu !

#### 3.0 One, Two, Three ... Replication

Il est utile de recuperer du contenu, mais le mieux est de le replication aussi connu sous le nom de pinner.
Cela va permettre d'ecrire de la metadata est d'exprimer que vous ne souhaitez pas supprimer le contenu.

A l'aide du CID, faites un pin du contenu.

REPLICATIONNNNN ! Nous sommes maintenant plusieurs a avoir notre contenu.
Plus vous avez de noeuds avec votre contenu pinner, plus vous allez avoir la recuperer et l'echange de contenu sera rapide.

Il existe des services de pinning qui vous permet d'utiliser des machines afin de pinner des contenu.

EXAMPLE : Pinata, Scaleway. Vous avez meme des blockchains dediee a recompenser par des Tokens les gens qui mettents a 
disposition leurs machines (Filecoin).

Verifier a l'aide de la commande `ipfs pin ls` que votre contenu est bien pin.

#### 4.0 Garbage Collector

Maintenant que notre contenu est pinner. Nous allons supprimer tous les blocks inutiles,
Il existe plusieurs type de garbage collector en informatique.
Le garbage collector en programmation qui vous permet de free votre memoire de maniere automatique commme le python ou le JS.
Et celui qui permet de supprimer des blocks sur les filesystems.
Devinez lequel nous allons utiliser :eyes:

Cette commande est un peu plus complique a trouver mais vous allez y arriver !
Le `gc`, n'est par defaut pas activer sur vos noeuds.

#### 5.0 Turn Off

Nous allons nous assurer de toujours avoir notre contenu, Mais avant ca pour ne pas etre biaiser, nous allons eteindre notre daemon.
Sinon, il est possible sans le savoir de recuperer le contenu d'un autre noeud.

#### 6.0 Unpin Content

Nous allons unpin notre CID.
Verifier bien a l'aide `ipfs pin ls` que votre cid n'est pas existant


#### 7.0 Back to the Past

Si toutes les etapes ce sont bien passe, nous ne devrions etre capable de faire passer le GC et voir nos blocs disparaitre a tout jamais.

### III. Pimp my node

Nous avons pu observer pas mal de souci sur notre neoud.

#### Automatic GC

Pourquoi notre GC ne passe pas par defaut ?
Nous allons parametrer notre noeud pour que notre GC passe toutes les 10 min.

N'oubliez pas de faire la commande `ipfs init` pour prendre en compte vos changement.

### II. Private Network

####



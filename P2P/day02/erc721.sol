pragma solidity 0.8.17;

// SPDX-License-Identifier: MIT

abstract contract ERC721 {
    /**
     * @dev Returns number of NFTs owned by an address.
     */
    function balanceOf(address _owner)
        public
        view
        virtual
        returns (uint256 _balance);

    /**
     * This function returns the address of the owner of a token.
     * As each ERC-721 token is unique and non-fungible,
     * they are represented on the blockchain by an ID. Other users,
     * contracts, apps can use this ID to determine the owner of the token
     */
    function ownerOf(uint256 _tokenId)
        public
        view
        virtual
        returns (address _owner);

    /**
     * @dev Transfers `tokenId` token from `from` to `to`.
     *
     * WARNING: Note that the caller is responsible to confirm that the recipient is capable of receiving ERC721
     * or else they may be permanently lost. Usage of {safeTransferFrom} prevents loss, though the caller must
     * understand this adds an external call which potentially creates a reentrancy vulnerability.
     *
     * Requirements:
     *
     * - `from` cannot be the zero address.
     * - `to` cannot be the zero address.
     * - `tokenId` token must be owned by `from`.
     * - If the caller is not `from`, it must be approved to move this token by either {approve} or {setApprovalForAll}.
     *
     * Emits a {Transfer} event.
     */
    function transfer(address _to, uint256 _tokenId) public virtual;

    /**
     * @dev Gives permission to `to` to transfer `tokenId` token to another account.
     * The approval is cleared when the token is transferred.
     *
     * Only a single account can be approved at a time, so approving the zero address clears previous approvals.
     *
     * Requirements:
     *
     * - The caller must own the token or be an approved operator.
     * - `tokenId` must exist.
     *
     * Emits an {Approval} event.
     */
    function approve(address _to, uint256 _tokenId) public virtual;

    /**
     * @dev This is an optional function that acts like a withdraw function since an outside party
     * can call it to take tokens out of another user’s account.
     *
     * Therefore, takeOwnership can be used when a user has
     * been approved to own a certain amount of tokens and wishes
     * to withdraw said tokens from another user’s balance.
     */
    function takeOwnership(uint256 _tokenId) public virtual;
}

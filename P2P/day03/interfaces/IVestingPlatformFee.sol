// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

interface IVestingPlatformFee {
    error NotEnoughBalance();
    error NotEnoughAllowance();

    /**
     * @notice Change the fee
     * @param newFee New fee
     */
    function changeFee(uint256 newFee) external;

    /**
     * @notice Change the fee address
     * @param newFeeAddress New fee address
     */
    function changeFeeAddress(address newFeeAddress) external;

    /**
     * @notice Get the fee
     * @return Fee
     */
    function fee() external view returns (uint256);

    /**
     * @notice Get the fee address
     * @return Fee address
     */
    function feeAddress() external view returns (address);

    /**
     * @notice Withdraw all vesting tokens from the contract to the owner
     */
    function withdraw() external;
}